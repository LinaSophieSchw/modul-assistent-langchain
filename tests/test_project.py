import unittest, json, os
from pathlib import Path
from modul_assistent.core import ROOT, lernzeit, load_pages, build_index, ask_rag, make_agent

class ProjectTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        os.environ['LLM_MODE']='demo'
        cls.store,cls.chunks=build_index()
    def test_literate_structure(self):
        notebooks=sorted((ROOT/'notebooks').glob('*.ipynb'))
        self.assertEqual(len(notebooks),4)
        for path in notebooks:
            cells=json.loads(path.read_text(encoding='utf-8'))['cells']
            for i,c in enumerate(cells):
                if c['cell_type']=='code':
                    self.assertEqual(cells[i-1]['cell_type'],'markdown',path.name)
            text='\n'.join(''.join(c['source']) for c in cells if c['cell_type']=='markdown')
            for title in ['Lernziele','Setup','Konzept','Experiment','Häufige Fehler','Prompt Logbuch','Zusammenfassung','Übungsaufgabe']:
                self.assertIn(title,text)
            self.assertFalse(''.join(cells[-1]['source']).strip())
    def test_real_pdf_metadata(self):
        pages=load_pages()
        self.assertEqual({d.metadata['source'] for d in pages},
                         {'Eigenschaften-Bitcoin.pdf','Open Banking_Zusammenfassung.pdf'})
        self.assertEqual(len(pages),5)
        self.assertTrue(all(d.metadata['seite']>=1 for d in self.chunks))
    def test_rag_sources(self):
        cases = [
            ('Auf welche Gesamtmenge ist Bitcoin begrenzt?', 'Eigenschaften-Bitcoin.pdf', 1, '21'),
            ('Welche Formate nennt die Unterlage für die Codierung?', 'Open Banking_Zusammenfassung.pdf', 1, 'JSON'),
            ('Welche Erlaubnis benötigen Drittanbieter für den Zugriff auf Bankdaten?', 'Open Banking_Zusammenfassung.pdf', 3, 'Bankdaten'),
        ]
        for question,filename,page,signal in cases:
            answer,_=ask_rag(question,self.store,k=8)
            self.assertEqual(answer.quelle,f'{filename}, S. {page}')
            self.assertIn(signal,answer.antwort)
    def test_abstention_and_unknown_fixture(self):
        answer,_=ask_rag('Wie hoch ist der Bitcoin-Kurs heute?',self.store,k=8)
        self.assertEqual(answer.quelle,'keine Quelle')
        with self.assertRaises(ValueError): ask_rag('Wie alt ist das Internet?',self.store)
    def test_tool_boundary(self):
        self.assertIn('90',lernzeit.invoke({'ects':3}))
        with self.assertRaises(ValueError): lernzeit.invoke({'ects':-1})
    def test_agent_executes_tool(self):
        result=make_agent(self.store).invoke({'input':'Planungswert für 3 ECTS'})
        self.assertIn('90',result['output'])
        self.assertEqual(result['intermediate_steps'][0][0].tool,'lernzeit')
    def test_agent_document_and_unknown_tools(self):
        agent = make_agent(self.store)
        known = agent.invoke({'input': 'Auf welche Gesamtmenge ist Bitcoin begrenzt?'})
        self.assertIn('Eigenschaften-Bitcoin.pdf, S. 1', known['output'])
        self.assertEqual(known['intermediate_steps'][0][0].tool, 'modul_suche')
        self.assertIn('21', known['intermediate_steps'][0][1])
        unknown = agent.invoke({'input': 'Wie hoch ist der Bitcoin-Kurs heute?'})
        self.assertIn('keine Quelle', unknown['output'])

    def test_demo_agent_does_not_invent_missing_reference(self):
        agent = make_agent(self.store)
        result = agent.invoke({'input': 'Wie viele gibt es davon maximal?'})
        self.assertFalse(result['intermediate_steps'])
        self.assertIn('Thema', result['output'])

if __name__=='__main__': unittest.main()
