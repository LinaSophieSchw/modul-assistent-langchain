"""Kleine Live-Prüfung der BFH-Verbindung, ohne PDF-Inhalte zu übertragen."""
from dotenv import load_dotenv
from modul_assistent.core import ROOT, mode, chat_model, embedding_model
load_dotenv(ROOT/'.env',override=True)
if mode() != 'bfh':
    raise SystemExit('Zuerst LLM_MODE=bfh in .env einstellen. Siehe README.')
reply = chat_model().invoke('Antworte auf Deutsch in einem kurzen Satz: Was ist ein Notebook?')
print(reply.content)
print('Tokenangaben:',reply.usage_metadata)
vector = embedding_model().embed_query('Ein Notebook verbindet Code und Erklärung.')
assert vector and all(isinstance(x,(int,float)) for x in vector)
print('Embedding-Dimension:',len(vector))
print('Chat und Embeddings erreichbar. Toolwahl und RAG separat in den Notebooks prüfen.')
