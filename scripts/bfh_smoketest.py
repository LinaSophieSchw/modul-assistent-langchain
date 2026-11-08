"""Kurze Prüfung von Chat und Embeddings über die BFH-Schnittstelle."""
from dotenv import load_dotenv
from modul_assistent.core import ROOT, chat_model, embedding_model

load_dotenv(ROOT / '.env', override=False)
reply = chat_model().invoke('Antworte auf Deutsch in einem kurzen Satz: Was ist ein Jupyter Notebook?')
print(reply.content)
print('Tokenangaben:', reply.usage_metadata)
vector = embedding_model().embed_query('Ein Notebook verbindet Code und Erklärung.')
assert vector and all(isinstance(x, (int, float)) for x in vector)
print('Embedding-Dimension:', len(vector))
print('BFH-Chat und BFH-Embeddings erreichbar. RAG und Werkzeugwahl werden in den Notebooks geprüft.')
