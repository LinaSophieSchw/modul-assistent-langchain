# LangChain durch Literate Programming lernen

Vier deutschsprachige Jupyter Notebooks bauen einen kleinen Modul-Assistenten auf.
Die Erklärungen, Experimente, absichtlichen Fehler und Übungen stehen direkt in den Notebooks.
Als Wissensbasis dienen zwei vorhandene PDF-Unterlagen zur DIFA-Projektarbeit.

## Lernpfad

| Notebook | Leitfrage | Ergebnis |
|---|---|---|
| [01](notebooks/01_hello_langchain_prompts.ipynb) | Wie wird aus einer Frage eine strukturierte Antwort? | Prompts, LCEL, Streaming und Tokenverbrauch |
| [02](notebooks/02_memory.ipynb) | Wie wird ein Gesprächsbezug mitgegeben? | Getrennte Sitzungen und Vergleich von Buffer, Window und Summary |
| [03](notebooks/03_rag.ipynb) | Wie findet der Assistent Belege? | Zwei PDFs, Chunks, Embeddings, Chroma und RetrievalQA |
| [04](notebooks/04_agents_evaluation.ipynb) | Wann hilft ein Tool und wie prüfe ich das Ergebnis? | ReAct, AgentExecutor, Lernzeitrechner und Mini-Evaluation |

Die Notebooks bauen inhaltlich aufeinander auf. Technisch startet jedes mit einem eigenen Setup
und läuft in einem frischen Kernel. Eine Codezelle wird immer direkt vorher erklärt.
Die letzte, leere Codezelle ist jeweils für eine eigene Übung gedacht.

## Start unter Windows

Voraussetzung ist Python **3.12**. Andere Versionen sind nicht geprüft.
ZIP entpacken und im Projektordner `setup.bat` doppelt anklicken.
Das Skript installiert die festgehaltenen Paketversionen und öffnet JupyterLab.
Bei erneutem Start wird dieselbe Umgebung verwendet.

Manuell in einer Eingabeaufforderung:

```bat
py -3.12 -m venv .venv
.venv\Scripts\python -m pip install -r requirements.txt
.venv\Scripts\python -m pip install -e .
.venv\Scripts\python -m jupyterlab notebooks
```

macOS und Linux: `bash setup.sh`. Auch dort wird Python 3.12 benötigt.
Nach dem Öffnen von Notebook 01 den Kernel der Projektumgebung wählen und alle Zellen ausführen.
Gespeicherte Ausgaben in den gelieferten Notebooks stammen aus dem lokalen Demo-Modus.

## Demo und BFH sind unterschiedliche Nachweise

Standard ist `LLM_MODE=demo`. Hier sind Antworten selbst geschriebene Testdaten und die
Embeddings Wort-Hashing. Es wird kein Modell heruntergeladen und keine API aufgerufen.
Die Demo zeigt den Programmablauf, keine Sprachmodellqualität. Es handelt sich nicht um
aufgezeichnete Antworten eines echten Modells. Neue Fragen brauchen neue Demo-Fälle oder den BFH-Modus.

Für echte Modellanfragen `.env.example` nach `.env` kopieren und anpassen:

```dotenv
LLM_MODE=bfh
BFH_API_KEY=dein_persoenlicher_schluessel
BFH_BASE_URL=https://inference.mlmp.ti.bfh.ch/api/v1
BFH_CHAT_MODEL=gpt-oss:120b
BFH_EMBEDDING_MODEL=embeddinggemma:300m
```

Der Schlüssel wird unter https://access.mlmp.ti.bfh.ch erzeugt. Er gehört nur in `.env`.
Ausserhalb des BFH-Netzes nennt die Dokumentation den Proxy
`https://inference.proxy.ti.bfh.ch`; für die API wird ebenfalls `/api/v1` verwendet.
Modellnamen und Erreichbarkeit vor dem Live-Lauf anhand der
[BFH-Dokumentation](https://infra.pages.ti.bfh.ch/mlmp/src/llm/) prüfen.
Die Beispiele verwenden die OpenAI-kompatible Chat-Completions-Schnittstelle.
`ChatOpenAI` ist hier der Client für den BFH-Dienst; ein zusätzlicher OpenAI-Schlüssel ist nicht erforderlich.

Nach dem Wechsel den Kernel neu starten und alle Zellen ausführen. Der Index wird neu aufgebaut.
Im Live-Modus werden PDF-Textabschnitte zum Embedding und zur Antwortgenerierung an die BFH gesendet.
Nur geeignete, freigegebene Unterlagen verwenden; die BFH weist auf den Ausschluss sensibler Daten hin.
Die Anfragezahl bleibt durch synchrone Ausführung klein. Bei Rate-Limit-Fehlern eine Pause machen.

Vor der ersten vollständigen Live-Ausführung:

```bat
.venv\Scripts\python scripts\bfh_smoketest.py
```

Dieser Test prüft Chat und Embeddings mit kurzen unkritischen Beispielen. Er verändert keine Einstellungen.
Die Live-Anbindung ist implementiert, konnte ohne persönlichen BFH-Schlüssel aber nicht geprüft werden.

## Projekt prüfen

```bat
.venv\Scripts\python -m unittest discover -s tests -v
.venv\Scripts\python scripts\run_notebooks.py
```

Der zweite Befehl verwendet absichtlich immer den Demo-Modus, startet pro Notebook einen frischen
Python-Prozess und speichert die Ausgaben. Er lehnt eine lokale `.env` mit `LLM_MODE=bfh` ab,
damit ein automatisierter Test keine unbeabsichtigten API-Anfragen auslöst.
Für echte BFH-Versuche die Notebooks in Jupyter ausführen. Die CSV aus Notebook 04 trägt den Modus
im Dateinamen; automatische Signalprüfungen ersetzen keine manuelle Bewertung der Belegtreue.

## Vor der eigenen Abgabe

- In jedem Prompt-Logbuch den tatsächlich selbst formulierten Erstprompt ergänzen und mit der Endversion testen.
- Die persönliche Reflexion anhand der Fragen in [Abschlussreflexion](docs/Abschlussreflexion.md) verfassen.
- BFH-Läufe durchführen und die Antworten, Quellen und Toolentscheidungen manuell bewerten.
- KI-Unterstützung gemäss den Regeln des Moduls offenlegen. Ein Vorschlag steht in der Reflexionsdatei.
- PDF-Unterlagen nur veröffentlichen, wenn deren Weitergabe erlaubt ist. Bei Bedarf vor einem öffentlichen Upload entfernen und lokal wieder in `data/` ablegen.

## Dokumentation und Entscheidungen

- [Anforderungen und Nachweise](docs/Anforderungen.md)
- [Schriftliche Einordnung der Hausarbeit](docs/Hausarbeit.md)
- [Einordnung der Vorlage und der E-Mail](docs/Vorlage_und_Feedback.md)
- [Technische Entscheidungen und Grenzen](docs/Architektur.md)
- [Abschlussreflexion und Erweiterungen](docs/Abschlussreflexion.md)
- [Prüfprotokoll](docs/Pruefprotokoll.md)

Die in der Aufgabe genannten älteren APIs `RetrievalQA`, `create_react_agent` und
`AgentExecutor` liegen inzwischen in `langchain-classic`. Sie werden bewusst gezeigt, um den
Auftrag abzubilden. Für neue Anwendungen zeigt die offizielle Dokumentation `create_agent`.

## Quellen

Didaktische Anregung: Raquel Kehl, *Learning LangGraph through Literate Notebooks*,
https://github.com/RaquelKehl/learn-langgraph-literate-notebooks, eingesehener Stand
`b5dc4e94c2767b651470ce0fd8966a1145f92a69`, abgerufen am 30.10.2026.
Übernommen sind Gestaltungsprinzipien wie ein durchgehender Fall und dokumentierte Fehler;
Code und Notebooktexte dieses Projekts wurden neu erstellt. Die Vorlage ist englisch,
dieser Lernpfad deutsch und auf die LangChain-Aufgabe mit vier Notebooks zugeschnitten.

Offizielle Dokumentation:
- https://docs.langchain.com/oss/python/langchain/overview
- https://docs.langchain.com/oss/python/integrations/chat/openai
- https://docs.langchain.com/oss/python/integrations/embeddings/openai
- https://docs.langchain.com/oss/python/integrations/vectorstores/chroma
- https://reference.langchain.com/python/langchain-classic/agents/
- https://infra.pages.ti.bfh.ch/mlmp/src/llm/

Literate Programming: Donald E. Knuth (1984), *Literate Programming*, The Computer Journal,
27(2), 97–111, https://doi.org/10.1093/comjnl/27.2.97.
Die konkrete Anforderung ergibt sich aus den beiden PDFs in `data/`.
