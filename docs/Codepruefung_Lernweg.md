# Warum manches im Notebook kompliziert wirkt

Diese Prüfung unterscheidet die Vorgaben der Aufgabenstellung von zusätzlichen Projektentscheidungen. Sie begründet den Lernweg, ohne den funktionierenden Code während des gemeinsamen Durcharbeitens erneut umzubauen.

| Stelle | Einordnung | Konsequenz für das gemeinsame Lernen |
|---|---|---|
| Erklärungen vor Code, vier Notebooks, Lehrfehler und Übungen | Pflicht der Aufgabenstellung | Diese Abschnitte bleiben der rote Faden. |
| Besonders kurze Codezellen | Wunsch für dieses Projekt | Die Zeilengrenze ist keine Vorgabe des Dozenten; zusammengehörige Zellen werden gemeinsam erklärt. |
| Demo- und BFH-Modus | Zusätzliche Testmöglichkeit | Zuerst klären, welcher Modus läuft. Nur BFH erzeugt echte Modellantworten. Demo-Texte sind von Hand vorbereitet. |
| Pfade, Umgebungsvariablen und Modellparameter | Nötige Einrichtung, aber nicht das fachliche Hauptziel | Einmal verstehen, dann in späteren Notebooks nur wiedererkennen. Den API-Schlüssel niemals zeigen. |
| JSON und Parser in Notebook 01 | Festes Antwortschema ist gefordert | Datenform und inhaltliche Richtigkeit unterscheiden. |
| JSON und mehrere Vorlagen im Memory-Vergleich | Zusätzliche Fortführung des Schemas | Beim ersten Lesen auf die tatsächlich übergebenen Nachrichten konzentrieren; die JSON-Verpackung separat erklären. |
| Buffer, Window, Summary und getrennte Sitzungen | Pflicht | Speicherinhalt ansehen; die Modellantwort allein beweist keine richtige Speicherung oder Interpretation. |
| RunnableWithMessageHistory und InMemoryChatMessageHistory | Gewählte, inzwischen veraltete Implementierung | Die Warnungen erklären; sie sind keine Abbrüche. Diese konkreten Klassen sind nicht namentlich vorgeschrieben. |
| Direkte Vektorsuche und Retriever in Notebook 03 | Zwei Perspektiven auf denselben Suchschritt | Zuerst den Weg über den Retriever verstehen, danach den direkten Vergleich als Vertiefung lesen. |
| Vektorgrafik | Ausdrücklich gefordert | Die Grafik erklären, einschliesslich der Informationsverluste einer zweidimensionalen Projektion. |
| RetrievalQA, ReAct und AgentExecutor | Ausdrücklich in der Aufgabenstellung genannt | Die klassische Schnittstelle ist hier eine begründete Wahl. Nicht jede ältere API ist deshalb ein Aufgabenfehler. |
| Agentenaufbau in Notebook 04 | Werkzeuge, Prompt und Executor werden lokal aufgebaut | Der frühere Text zu make_agent war an dieser Stelle veraltet und wurde korrigiert. |
| CSV-Export und automatische Wortprüfung | Zusatz zur geforderten systematischen Bewertung | Zuerst einen einzigen Fall von Hand bewerten. Die Schleife wiederholt das Vorgehen; ein passendes Wort beweist keine korrekte Antwort. |
| Vorbereitete Promptformulierungen | Erklär- und Übungshilfe | Sie sind KI-Vorschläge. Die Aufgabenstellung verlangt zusätzlich einen tatsächlich selbstständig formulierten Erstprompt und reale Beobachtungen. |

## Drei Fragen für jede Codezelle

1. **Was liegt vorher vor?** Beispielsweise eine Frage als Text, eine Nachrichtenliste oder gefundene PDF-Abschnitte.
2. **Was verändert diese Zelle?** Beispielsweise Nachrichten ergänzen, das Modell aufrufen oder eine Antwort auslesen.
3. **Was liegt danach vor?** Den tatsächlichen Wert oder dessen Typ ansehen, statt nur auf eine fehlende Fehlermeldung zu vertrauen.

## Beobachtete Grenzen, die erklärt werden müssen

Im BFH-Memory-Test deutete das Modell eine spätere Sachfrage fälschlich als Antwortwunsch. Der Speicher war technisch getrennt und die Antwort formal lesbar; die Interpretation war trotzdem falsch. Im RAG-Test genügte der richtige Seitenname zunächst nicht, weil der benötigte Tabellenabschnitt im Kontext fehlte. Beim Agenten wurde fehlendes Wissen korrekt ausgedrückt, aber das verlangte Quellenformat einmal nicht exakt eingehalten.

Diese Befunde bleiben sichtbar. Sie sind Lernmaterial und werden weder ausgeblendet noch durch vorbereitete erfolgreiche Modellantworten ersetzt.

Grundlage: LangChain_Literate_Programming_Aufgabenstellung.pdf, insbesondere Abschnitte 4 bis 9; Prüfung des lokalen Projektstands vom 5. November 2026.
