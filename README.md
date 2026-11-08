# LangChain durch Literate Programming lernen

Vier deutschsprachige Jupyter Notebooks bauen einen kleinen Modul-Assistenten auf.
Die Erklärungen, Experimente, absichtlichen Fehler und Übungen stehen direkt in den Notebooks.
Als Wissensbasis dienen zwei kurze DIFA-Kursunterlagen in `data/modulunterlagen`:
`Eigenschaften-Bitcoin.pdf` (eine Seite) und `Open Banking_Zusammenfassung.pdf` (vier Seiten).
Notebook 01 liest die Bitcoin-PDF direkt; die spätere Suche verwendet beide PDFs.
Die Aufgaben-PDFs im übergeordneten Ordner `data/` bleiben Projektvorgaben und gehören nicht zum Suchkorpus.

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

Das Projekt unterstützt Python **3.12 und 3.13**. Die folgende Anleitung verwendet
Python **3.13**. Die tatsächlich durchgeführten Prüfungen stehen in
[Prüfprotokoll](docs/Pruefprotokoll.md). Andere Versionen sind nicht freigegeben.
ZIP entpacken und im Projektordner `setup.bat` doppelt anklicken.
Das Skript installiert die festgehaltenen Paketversionen und öffnet JupyterLab.
Bei erneutem Start wird dieselbe Umgebung verwendet.

Manuell in einer Eingabeaufforderung:

```bat
py -3.13 -m venv .venv
.venv\Scripts\python -m pip install -r requirements.txt
.venv\Scripts\python -m pip install -e .
.venv\Scripts\python -m jupyterlab notebooks
```

macOS und Linux: `bash setup.sh` verwendet Python 3.13. Für Python 3.12 kann
`PYTHON_BIN=python3.12 bash setup.sh` verwendet werden. Diese Systeme sind nicht getestet.
Nach dem Öffnen von Notebook 01 den Kernel der Projektumgebung wählen und alle Zellen ausführen.
Notebook 01 enthält nach der Korrektur der BFH-Adresse keine gespeicherten Ausgaben;
die erste eigene BFH-Ausführung kann so von oben begonnen werden. Die gespeicherten
Ausgaben der übrigen Notebooks stammen aus dem lokalen Demo-Modus.

## Demo und BFH sind unterschiedliche Nachweise

Standard ist `LLM_MODE=demo`. Hier sind Antworten selbst geschriebene Testdaten und die
Embeddings Wort-Hashing. Es wird kein Modell heruntergeladen und keine API aufgerufen.
Die Demo zeigt den Programmablauf, keine Sprachmodellqualität. Es handelt sich nicht um
aufgezeichnete Antworten eines echten Modells. Neue Fragen brauchen neue Demo-Fälle oder den BFH-Modus.

Für echte Modellanfragen `.env.example` nach `.env` kopieren und anpassen:

```dotenv
LLM_MODE=bfh
BFH_API_KEY=dein_persoenlicher_schluessel
BFH_BASE_URL=https://inference.proxy.ti.bfh.ch/v1
BFH_CHAT_MODEL=gpt-oss:120b
BFH_EMBEDDING_MODEL=embeddinggemma:300m
```

Der Schlüssel wird unter https://access.mlmp.ti.bfh.ch erzeugt. Er gehört nur in `.env`.
Die Dokumentation nennt für den Zugriff von ausserhalb den Proxy-Host.
Die für dieses Projekt geprüfte API-Basisadresse ist
`https://inference.proxy.ti.bfh.ch/v1`. Der Proxy wurde mit diesem API-Pfad geprüft;
`/api/v1` liefert dort einen HTTP-404-Fehler. Die Hostadresse allein und die
vollständige API-Basisadresse sind zu unterscheiden.
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
Ein kurzer echter Chat-Aufruf über den BFH-Proxy mit `qwen3.8-27b` wurde erfolgreich
geprüft. Die überarbeiteten Notebooks 02 bis 04 wurden inzwischen zusätzlich über BFH ausgeführt, einschliesslich echter Embeddings und Toolaufrufe. Zwei beobachtete Grenzen (Window-Fehlinterpretation und Quellenformat) sind in den Notebooks und im Prüfprotokoll dokumentiert. Einzelheiten stehen im Prüfprotokoll.

## Projekt prüfen

```bat
.venv\Scripts\python -m unittest discover -s tests -v
.venv\Scripts\python scripts\run_notebooks.py
```

Der zweite Befehl verwendet absichtlich immer den Demo-Modus, startet pro Notebook einen frischen
Python-Prozess und speichert die Ausgaben. Die explizite Demo-Einstellung des Testprozesses hat Vorrang vor `.env`, damit keine unbeabsichtigten API-Anfragen ausgelöst werden.
Für echte BFH-Versuche die Notebooks in Jupyter ausführen. Die CSV aus Notebook 04 trägt den Modus
im Dateinamen; automatische Signalprüfungen ersetzen keine manuelle Bewertung der Belegtreue.

## Vor der eigenen Abgabe

- In jedem Prompt-Logbuch den tatsächlich selbst formulierten Erstprompt ergänzen und mit der Endversion testen.
- Den ausformulierten [Reflexionsbericht](docs/Reflexionsbericht.pdf) mit den eigenen weiteren Beobachtungen ergänzen; die bearbeitbare Fassung steht in [Abschlussreflexion](docs/Abschlussreflexion.md).
- BFH-Läufe durchführen und die Antworten, Quellen und Toolentscheidungen manuell bewerten.
- KI-Unterstützung gemäss den Regeln des Moduls offenlegen. Ein Vorschlag steht in der Reflexionsdatei.
- PDF-Unterlagen nur veröffentlichen, wenn deren Weitergabe erlaubt ist. Bei Bedarf vor einem öffentlichen Upload entfernen und lokal wieder in `data/` ablegen.

## Dokumentation und Entscheidungen

- [Anforderungen und Nachweise](docs/Anforderungen.md)
- [Schriftliche Einordnung der Hausarbeit](docs/Hausarbeit.md)
- [Technische Entscheidungen und Grenzen](docs/Architektur.md)
- [Abschlussreflexion und Erweiterungen](docs/Abschlussreflexion.md)
- [Prüfprotokoll](docs/Pruefprotokoll.md)

Die in der Aufgabe genannten älteren APIs `RetrievalQA`, `create_react_agent` und
`AgentExecutor` liegen inzwischen in `langchain-classic`. Sie werden bewusst gezeigt, um den
Auftrag abzubilden. Für neue Anwendungen zeigt die offizielle Dokumentation `create_agent`.
