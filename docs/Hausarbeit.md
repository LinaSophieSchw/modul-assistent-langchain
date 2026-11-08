# Einen Modul Assistenten mit LangChain schrittweise aufbauen

## Ziel der Arbeit

Diese Arbeit bereitet zentrale LangChain-Konzepte so auf, dass eine Person mit Python-Grundkenntnissen
sie anhand von vier Jupyter Notebooks nachvollziehen und ausprobieren kann. Das Ergebnis ist ein
kleiner Modul-Assistent über zwei DIFA-Kursunterlagen zu Bitcoin und Open Banking. Der Schwerpunkt liegt auf
dem Verständnis des Datenflusses und auf begründeten Entscheidungen. Eine produktionsreife Anwendung
ist nicht das Ziel. Den verbindlichen Umfang legt die ausführliche Aufgabenstellung fest [1].

Die vier Notebooks sind die eigentliche Ausarbeitung. Dieser Text ordnet ihren Aufbau ein. Die
persönliche Abschlussreflexion wird getrennt ergänzt, weil technische Erklärungen eigene Erfahrungen
und eine tatsächlich selbst durchgeführte Prompt-Iteration nicht ersetzen können.

## Literate Programming als Arbeitsweise

Beim Literate Programming gehören Erklärung und Programm zusammen [2]. Für diese Arbeit bedeutet
das: Erst wird die Frage erklärt, dann folgt der Code. Die nächste Erklärung greift auf, was das
Experiment zeigt und welche Grenze noch offen bleibt. Eine Codezelle ohne direkt vorangehende
Begründung wäre deshalb auch dann unvollständig, wenn sie technisch funktioniert.




## Aufbau des Lernpfads

### Notebook 01

Der Einstieg verfolgt eine einzelne Nachricht von der Python-Eingabe bis zur strukturierten Antwort.
Die erste Seite der Bitcoin-PDF liefert den Kontext zu einer Frage nach der begrenzten Gesamtmenge.
Ein PromptTemplate verbindet diesen Text mit der Frage. Über den
LCEL-Operator werden Prompt, Modell und Parser zu einer Chain verknüpft. Die drei Schritte lassen
sich zusätzlich einzeln ausführen, damit der Datenfluss sichtbar bleibt.

Das Antwortschema trennt Antworttext und Quelle. Dadurch lässt sich die Form kontrollieren, ohne
eine inhaltliche Verlässlichkeit vorzutäuschen. Eine fehlende Promptvariable wird als konkretes Fehlerbeispiel reproduziert und korrigiert.
Der Parser erklärt zusätzlich, wie eine vorgegebene Antwortform geprüft wird.
Streaming und die Kostenrechnung ergänzen den Blick auf den Modellaufruf. Die Beispielpreise sind
Rechenannahmen; ein BFH-Tarif wird daraus nicht abgeleitet.

### Notebook 02

Die Anschlussfrage «Was kommt im dritten?» zeigt die Grenze eines einzelnen Aufrufs. Der
Gesprächsbezug entsteht erst, wenn die bisherigen Nachrichten wieder mitgesendet werden.
RunnableWithMessageHistory übernimmt diese Verbindung zwischen Chain und Sitzungsspeicher.
Eine session_id ordnet Nachrichten dem richtigen Gespräch zu. Sie ersetzt keine Benutzeranmeldung.

Buffer erhält den vollständigen Verlauf, Window begrenzt ihn auf die letzten Gesprächspaare,
Summary verdichtet ihn inhaltlich. Keine Variante ist grundsätzlich die beste. Die Auswahl hängt
davon ab, ob Wortlaut, jüngste Aufgabe oder längerfristiger Sachstand wichtig sind. Für das kleine
Beispiel ist Buffer die einfachste nachvollziehbare Wahl. Die anderen Varianten zeigen, welche
Informationen bei einer Begrenzung verloren gehen können.

### Notebook 03

Gesprächsverlauf ist noch keine fachliche Quelle. Deshalb ergänzt das dritte Notebook eine
RAG-Pipeline über die beiden Kursunterlagen zu Bitcoin und Open Banking.
Die Texte werden mit einem PDF-Loader seitenweise geladen. Ein Splitter bildet überlappende
Abschnitte, ein Embedding-Verfahren erzeugt Vektoren, und Chroma verwaltet den Suchindex.

Die erste Konfiguration verwendet 900 Zeichen pro Chunk und 150 Zeichen Überlappung. Dies sind
begründete Startwerte, keine empirisch optimierten Parameter. Der Retriever liefert passende
Abschnitte, die gemeinsam mit der Frage an das Modell gehen. Die in der Aufgabe genannte
RetrievalQA-Schnittstelle wird ausdrücklich gezeigt. Für das feste Antwortschema kommt danach
wieder die LCEL-Chain aus dem ersten Notebook zum Einsatz.

Dateiname und Seitennummer bleiben an den Abschnitten erhalten. Eine ausgegebene Quellenangabe
wird gegen diese Metadaten geprüft. Damit lässt sich eine erfundene Herkunft abweisen. Ob die
Antwort die Textstelle korrekt wiedergibt, muss weiterhin inhaltlich bewertet werden. Auch ein
korrekter Seitenverweis kann eine unzutreffende Aussage begleiten.

### Notebook 04

Der letzte Schritt ergänzt einen Lernzeitrechner als eigenes Tool. Er berechnet einen Planungswert
von 30 Stunden pro ECTS. Der Wert ist eine explizite Annahme des Beispiels und keine aus den
Unterlagen entnommene Modulvorschrift. Diese Unterscheidung gehört sowohl in die Toolbeschreibung
als auch in die endgültige Antwort.

Ein begrenzter ReAct-Agent kann zwischen Dokumentensuche und Rechner wählen. Die sichtbaren
Schritte nennen Werkzeug, Eingabe und Rückgabe. Eine kurze ausgegebene Begründung der Toolwahl
ist dabei keine Offenlegung interner Modellüberlegungen. Gesprächsverwaltung, Dokumentensuche und
Toolnutzung werden zu einem kleinen Assistenten verbunden. Für reine Dokumentfragen bleibt die
feste RAG-Chain einfacher zu prüfen. Ein Agent wird erst dann interessant, wenn die passende Aktion
von der Frage abhängt.

## Anbindung an den BFH Dienst

Chat und Embeddings verwenden im Live-Modus die dokumentierte BFH-Inference-Schnittstelle [4].
Der persönliche Schlüssel, die Basis-URL und die Modellnamen liegen in einer lokalen .env-Datei.
Die Beispiele verwenden gpt-oss:120b für Chat und embeddinggemma:300m für Embeddings. Beide Namen
müssen vor einem späteren Live-Versuch erneut auf Verfügbarkeit geprüft werden.

ChatOpenAI dient hier als Client für eine OpenAI-kompatible Schnittstelle [5]. Die Anfrage geht an
den konfigurierten BFH-Endpunkt. Die konkret in der Aufgabe genannten älteren Chain- und
Agentenklassen werden über langchain-classic eingebunden. Diese Kompatibilitätsentscheidung ist
im Repository erläutert; die aktuelle LangChain-Einführung verwendet create_agent [6].

Ohne persönlichen Schlüssel kann die Anbindung implementiert und konfiguriert, aber nicht als
erfolgreich getestet gelten. Deshalb enthält das Repository einen kurzen Verbindungstest und
getrennte Ergebnisdateien für Demo und Live. Beim Wechsel des Embedding-Verfahrens wird der
Suchindex neu aufgebaut, weil Vektoren unterschiedlicher Modelle nicht gemeinsam verglichen werden sollen.

## Evaluation und Aussagegrenzen

Die Mini-Evaluation legt die Fragen vor dem Durchlauf fest: die begrenzte Bitcoin-Menge,
Codierungsformate in Open Banking, die Erlaubnis für den Datenzugriff, eine nicht beantwortbare
Frage nach dem heutigen Bitcoin-Kurs und eine Rechenfrage. Für Dokumentfragen
werden erwartete Seiten und einfache Antwortsignale hinterlegt. Beim Toolfall wird zusätzlich
geprüft, ob das Werkzeug tatsächlich ausgeführt wurde. Laufzeiten werden unmittelbar gemessen.

Die automatischen Prüfungen beurteilen nur diese vorgegebenen Kriterien. Ein passendes Wort im
Antworttext reicht nicht für eine korrekte Antwort. Die CSV-Datei enthält deshalb ein Feld für die
anschliessende manuelle Inhaltsprüfung. Ein sinnvoller nächster Versuch besteht aus mehreren
BFH-Durchläufen derselben Fragen und zusätzlichen, vorher nicht im Beispiel verwendeten Fragen.

Der lokale Modus verwendet konstruierte Antworten und lexikalisches Wort-Hashing. Seine erfolgreichen
Prüfungen belegen, dass bekannte Programmschritte zusammenarbeiten. Sie messen weder die Qualität
eines BFH-Modells noch die semantische Güte der Embeddings. Eine zweite Grenze ist der kleine
Dokumentenbestand: Der Assistent kennt die beiden Kursunterlagen, nicht alle Inhalte von Digital Finance.

## Einordnung des Ergebnisses

Der Lernpfad macht sichtbar, welche zusätzliche Funktion jeder Baustein übernimmt. Ein besserer
Prompt ersetzt keine fehlende Informationsbasis. Memory ersetzt keine Dokumentensuche. Eine
Quellenangabe ersetzt keine inhaltliche Prüfung. Ein Tool liefert nur unter seinen angegebenen
Annahmen ein belastbares Ergebnis. Diese Unterschiede sind für den kleinen Assistenten wichtiger
als möglichst viele Frameworkfunktionen einzubauen.

Die persönlichen Erstprompts, tatsächlichen BFH-Versuche und eigenen Lernerfahrungen werden vor
der Abgabe ergänzt. Zwei konkrete Erweiterungen sind bereits in der Reflexionsdatei ausgearbeitet:
die Erschliessung von Grafiken mittels Texterkennung und eine grössere systematische
Prüfung der Belegtreue.

## Literatur und Materialien

[1] LangChain durch Literate Programming erlernen. Bereitgestellte Aufgabenstellung, vier Seiten,
Datei data/LangChain_Literate_Programming_Aufgabenstellung.pdf. Ergänzend: DIFA-Projekte 2027,
Gruppen C und D, data/DIFA-Projekt 2027_Gruppen C und D.pdf.

[2] Knuth, D. E. (1984). Literate Programming. The Computer Journal, 27(2), 97–111.
https://doi.org/10.1093/comjnl/27.2.97. Grundkonzept gemäss der bereitgestellten Aufgabenstellung.

[4] BFH TI. Machine Learning Management Platform Inference API.
https://infra.pages.ti.bfh.ch/mlmp/src/llm/. Abruf 30.10.2026.

[5] LangChain. ChatOpenAI integration.
https://docs.langchain.com/oss/python/integrations/chat/openai. Abruf 30.10.2026.

[6] LangChain. LangChain overview.
https://docs.langchain.com/oss/python/langchain/overview. Abruf 30.10.2026.

[7] LangChain. Chroma integration.
https://docs.langchain.com/oss/python/integrations/vectorstores/chroma. Abruf 30.10.2026.

[8] LangChain. OpenAIEmbeddings integration.
https://docs.langchain.com/oss/python/integrations/embeddings/openai. Abruf 30.10.2026.
