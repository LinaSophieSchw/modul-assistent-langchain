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
        self.assertEqual(len({d.metadata['source'] for d in load_pages()}),2)
        self.assertTrue(all(d.metadata['seite']>=1 for d in self.chunks))
    def test_rag_sources(self):
        for question,page in [('Wie viele eigenständig lauffähige Notebooks sind gefordert?',1),
            ('Wie lang soll die Abschlussreflexion sein?',4),('Wie viele typische Fehler sollen pro Notebook gezeigt werden?',2)]:
            answer,_=ask_rag(question,self.store,k=8)
            self.assertIn(f'S. {page}',answer.quelle)
    def test_abstention_and_unknown_fixture(self):
        answer,_=ask_rag('In welcher Sprache muss die Abschlusspräsentation gehalten werden?',self.store,k=8)
        self.assertEqual(answer.quelle,'keine Quelle')
        with self.assertRaises(ValueError): ask_rag('Wie alt ist das Internet?',self.store)
    def test_tool_boundary(self):
        self.assertIn('90',lernzeit.invoke({'ects':3}))
        with self.assertRaises(ValueError): lernzeit.invoke({'ects':-1})
    def test_agent_executes_tool(self):
        result=make_agent(self.store).invoke({'input':'Planungswert für 3 ECTS'})
        self.assertIn('90',result['output'])
        self.assertEqual(result['intermediate_steps'][0][0].tool,'lernzeit')
if __name__=='__main__': unittest.main()
