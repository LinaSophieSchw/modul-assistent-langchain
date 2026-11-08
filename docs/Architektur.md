# Technische Entscheidungen und Grenzen

## Datenfluss

PDFs werden seitenweise geladen, mit Seitenmetadaten in Chunks geteilt, eingebettet und in
Chroma abgelegt. Der Retriever liefert Textabschnitte. Eine LCEL-Chain aus Prompt, Chatmodell
und Pydantic-Parser erzeugt Antwort und Quelle. Die Herkunft wird gegen die gefundenen
Abschnitte geprüft. Das sichert die Existenz einer Quelle, nicht die logische Ableitung jeder Aussage.

Der Agent kann modul_suche oder lernzeit verwenden. modul_suche ruft die RAG-Chain auf.
lernzeit rechnet unter einer expliziten Planungsannahme. Der Agent hat maximal vier Iterationen
und eine Laufzeitgrenze. Ungültiges ReAct-Format wird als Fehler sichtbar; es gibt keinen stillen
Wechsel auf einen scheinbar erfolgreichen anderen Ablauf.

## Warum Classic

Die Aufgabenstellung verlangt RetrievalQA und AgentExecutor. Die Implementierung verwendet
deshalb langchain-classic. Dies ist eine bewusste Kompatibilitätsentscheidung; es ist keine
Empfehlung, neue grössere Anwendungen grundsätzlich mit den alten APIs zu beginnen.
Die offizielle aktuelle Einführung verwendet create_agent. Der Vergleich ist im Notebook erläutert.

## Warum ein lokaler Modus

Ein persönlicher API-Schlüssel sollte keine Voraussetzung sein, um Erklärung, Datenfluss und
Fehlerfälle nachzuvollziehen. Die Demo nutzt konstruierte Antworten und lexikalische Vektoren.
Im BFH-Modus werden Chat und Embeddings ausgetauscht, während der übrige Datenfluss gleich bleibt.
Ein neuer Embedding-Raum braucht einen neu aufgebauten Index. Die Demo ist kein Modellbenchmark.

## Warum diese Unterlagen

Die zwei Kursunterlagen unter `data/modulunterlagen` behandeln Bitcoin und Open Banking.
Die kurze Bitcoin-Unterlage ermöglicht einen einfachen Einstieg. Die Open-Banking-Unterlage
ergänzt das Beispiel um APIs, Bankrollen und Datenaustausch. Die spätere Suche muss deshalb
passende Abschnitte aus der richtigen Datei auswählen. Die Aufgabenunterlagen in `data/`
werden nicht indexiert. Eingebettete Grafiken, insbesondere auf Seite 3 der Open-Banking-PDF,
sind beim einfachen Textauslesen teilweise nicht erfasst. Der Assistent deckt nur die
vorliegenden Inhalte ab; die Unterlagen werden nicht als aktuelle Markt- oder Rechtsauskunft verwendet.

## Weitere Grenzen

Der Speicher ist lokal und nicht dauerhaft. Sitzungskennungen sind keine Autorisierung.
Der Quellencheck verhindert keine inhaltlich falsche Antwort mit existierender Quellenangabe.
Textanweisungen im PDF werden im Prompt als Daten gekennzeichnet, eine umfassende Abwehr
von Prompt Injection ist damit nicht nachgewiesen. Die PDF-Extraktion enthält keine OCR.
Die BFH-Kompatibilität von ReAct-Format, Streaming und Embeddings ist erst durch Live-Läufe belegt.
Die festgehaltenen Paketversionen wurden unter Windows mit Python 3.12 und 3.13 geprüft.
Andere Systeme und spätere Paketupdates müssen gesondert validiert werden.
