# Aufbau des Modul Assistenten

## Modellanbindung

Alle Sprachmodell- und Embedding-Aufrufe verwenden die BFH-API. `chat_model()` erzeugt ein ChatOpenAI-Objekt für die konfigurierte BFH-Adresse. `embedding_model()` erzeugt OpenAIEmbeddings für denselben Dienst. Die Klassennamen bezeichnen kompatible LangChain-Adapter; sie legen keinen OpenAI-Server fest.

Adresse, Modellnamen und Schlüssel werden aus der lokalen Konfiguration gelesen. Der Schlüssel gehört in .env oder eine Umgebungsvariable und wird nicht ausgegeben. Ohne Schlüssel erscheint ein erklärender Fehler. API-Fehler werden nicht durch andere Antworten ersetzt.

## Lernpfad

1. Notebook 01: Text und Frage → Prompt → BFH-Modell → Parser → Antwort und Quelle.
2. Notebook 02: Frühere Nachrichten werden je Sitzung gespeichert und ausgewählt oder zusammengefasst erneut mitgegeben. Der Speicher gehört zum Programm, nicht zum Modell.
3. Notebook 03: PDF-Seiten → Abschnitte → BFH-Embeddings → Chroma → gefundene Abschnitte → BFH-Antwort mit Quelle.
4. Notebook 04: Ein Agent mit Gesprächsverlauf wählt Dokumentensuche oder Rechenwerkzeug. Der Executor führt den tatsächlichen Toolaufruf aus und gibt dessen Ergebnis zurück.

## Grenzen und Entscheidungen

Die Quelle wird mit den tatsächlich gefundenen Abschnitten abgeglichen. Diese Herkunftsprüfung ersetzt keine inhaltliche Belegprüfung. Ein gefundenes Dokument ist noch kein ausreichender Beleg für jede Frage.

Der Suchindex wird im Notebook neu aufgebaut. Wiederholte Notebookläufe erzeugen deshalb auch neue Embedding-Anfragen. Die Vektorgrafik reduziert die Darstellung auf zwei Dimensionen; Abstände darin bilden den ursprünglichen Raum nur teilweise ab.

RetrievalQA, create_react_agent und AgentExecutor werden zur ausdrücklich benannten Aufgabenstellung passend aus langchain-classic verwendet. Die im Memory-Beispiel eingesetzten Klassen erzeugen in der festgehaltenen Umgebung Veraltungswarnungen; diese werden erklärt.

Der Agent ist auf vier Iterationen begrenzt. Sein Zeitbudget ist kein harter Abbruch einer bereits laufenden Anfrage. Zusätzlich gibt es einen Timeout für den HTTP-Aufruf.

## Prüfungen

Die lokalen Tests prüfen Struktur, Schemas, PDF-Metadaten und den Rechner ohne API-Aufruf. Die Ausführung der Notebooks und der BFH-Verbindungstest verwenden echte Anfragen. Die Evaluation speichert tatsächliche Antworten und Werkzeugergebnisse; einfache Wort- und Quellenkriterien müssen manuell eingeordnet werden.

Für die Dokumentensuche als Agentenwerkzeug wird das Antwortschema direkt an die BFH-Schnittstelle übergeben (with_structured_output mit json_schema). Die API-Unterstützung wurde am 8. November durch einen echten Aufruf geprüft. Notebook01 erklärt zusätzlich den expliziten OutputParser; Notebook03 baut RetrievalQA mit Parser sichtbar auf. Notebook02 verwendet einfache Textantworten, damit der Gesprächsverlauf im Mittelpunkt steht.
