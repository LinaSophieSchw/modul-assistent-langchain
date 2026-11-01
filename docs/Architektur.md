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

Die zwei vorhandenen PDF-Dateien sind echte Aufgabenunterlagen und ermöglichen Fragen zu
Projektziel, Umfang und Anforderungen. Die allgemeine Übersicht enthält auch andere Projekte;
das macht eine sorgfältige Auswahl der Treffer nötig. Der Assistent deckt dadurch nicht sämtliche
Inhalte des Moduls Digital Finance ab. Andere Foliensätze können die PDFs ersetzen, benötigen aber
neue Sollfragen, Seitenbelege und entsprechend angepasste Demo-Fälle.

## Weitere Grenzen

Der Speicher ist lokal und nicht dauerhaft. Sitzungskennungen sind keine Autorisierung.
Der Quellencheck verhindert keine inhaltlich falsche Antwort mit existierender Quellenangabe.
Textanweisungen im PDF werden im Prompt als Daten gekennzeichnet, eine umfassende Abwehr
von Prompt Injection ist damit nicht nachgewiesen. Die PDF-Extraktion enthält keine OCR.
Die BFH-Kompatibilität von ReAct-Format, Streaming und Embeddings ist erst durch Live-Läufe belegt.
Die gelockten Paketversionen wurden für Python 3.12 unter Windows geprüft; andere Systeme
und spätere Paketupdates müssen gesondert validiert werden.
