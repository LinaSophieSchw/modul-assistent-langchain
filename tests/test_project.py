"""Lokale Struktur- und Funktionstests ohne Modellaufrufe."""
import json
import os
import unittest
from unittest.mock import patch
from langchain_text_splitters import RecursiveCharacterTextSplitter
from modul_assistent.core import ROOT, Antwort, lernzeit, load_pages, chat_model, embedding_model


class ProjectTests(unittest.TestCase):
    def test_literate_structure(self):
        notebooks = sorted((ROOT / 'notebooks').glob('*.ipynb'))
        self.assertEqual(len(notebooks), 4)
        for path in notebooks:
            cells = json.loads(path.read_text(encoding='utf-8'))['cells']
            for i, cell in enumerate(cells):
                if cell['cell_type'] == 'code':
                    self.assertEqual(cells[i - 1]['cell_type'], 'markdown', path.name)
                    compile(''.join(cell['source']), path.name, 'exec')
            text = '\n'.join(''.join(c['source']) for c in cells if c['cell_type'] == 'markdown')
            for title in ['Lernziele', 'Setup', 'Konzept', 'Experiment', 'Häufige Fehler',
                          'Prompt Logbuch', 'Zusammenfassung', 'Übungsaufgabe']:
                self.assertIn(title, text)
            self.assertFalse(''.join(cells[-1]['source']).strip())

    def test_pdf_metadata_and_chunks(self):
        pages = load_pages()
        self.assertEqual(len(pages), 5)
        self.assertEqual({p.metadata['source'] for p in pages},
                         {'Eigenschaften-Bitcoin.pdf', 'Open Banking_Zusammenfassung.pdf'})
        chunks = RecursiveCharacterTextSplitter(chunk_size=900, chunk_overlap=150).split_documents(pages)
        self.assertGreater(len(chunks), len(pages))
        self.assertTrue(all(c.metadata['seite'] >= 1 for c in chunks))

    def test_invalid_chunk_configuration(self):
        with self.assertRaises(ValueError):
            RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=150)

    def test_missing_key_is_explained(self):
        with patch.dict(os.environ, {'BFH_API_KEY': ''}):
            for factory in [chat_model, embedding_model]:
                with self.assertRaisesRegex(ValueError, 'BFH_API_KEY'):
                    factory()

    def test_answer_schema(self):
        answer = Antwort(antwort='Eine kurze Antwort.', quelle='Unterlage.pdf, S. 1')
        self.assertEqual(set(answer.model_dump()), {'antwort', 'quelle'})

    def test_tool_boundary(self):
        self.assertEqual(lernzeit.invoke({'ects': 3}),
                         'Planungswert: 90 Arbeitsstunden bei 30 Stunden pro ECTS.')
        for value in [-1, 0, 31]:
            with self.assertRaises(ValueError):
                lernzeit.invoke({'ects': value})


if __name__ == '__main__':
    unittest.main()
