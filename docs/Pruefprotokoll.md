# Prüfprotokoll der BFH Fassung

Stand: 8. November 2026. Frühere Arbeitsstände liegen ausserhalb des Repositorys als Sicherung. Dieses Protokoll beschreibt die aktuelle Fassung.

## Ausführung

Alle Chat- und Embedding-Anfragen gehen an die konfigurierte BFH-Schnittstelle. Es gibt keine Umschaltvariable und keine vorbereiteten Modellantworten. Ein fehlender Schlüssel wird vor dem Modellaufruf erklärt; API-Fehler bleiben sichtbar.

## Lokale Prüfungen

Sechs Tests prüfen ohne Modellanfragen: alle acht Notebookabschnitte und Python-Syntax, PDF-Metadaten samt Chunkbildung, ungültige Chunkkonfiguration, verständliche Fehlermeldungen bei fehlendem Schlüssel, Antwortschema und Grenzen des Rechenwerkzeugs. Diese Tests beurteilen keine Modellqualität.

## BFH Verbindung

Am 8. November wurden eine Chat-Antwort und ein Embedding tatsächlich vom BFH-Dienst empfangen. Das Embedding besitzt 768 Dimensionen. Ein erreichbarer Dienst allein beweist keine korrekte Antwort auf Fachfragen.

## Notebook Prüfung

Die vier umgestellten Notebooks werden nacheinander in frischen Kerneln ausgeführt. Der abschliessende Lauf wird nach Abschluss hier ergänzt. Gespeicherte Ausgaben stammen ausschliesslich aus tatsächlich ausgeführten BFH-Anfragen; die Übungszellen bleiben leer.

## Bisher beobachtete Grenzen

In einer früheren echten BFH-Einzelprobe verwechselte das Modell beim Window-Vergleich eine Sachfrage mit einem Antwortwunsch. Bei der Suche fehlte zunächst ein Tabellenabschnitt trotz passendem Seitennamen; die Auswahl wurde auf acht Treffer erweitert. Bei einer unbekannten Kursfrage drückte das Modell Nichtwissen korrekt aus, übernahm die verlangte Quellenzeichenfolge aber nicht exakt. Diese Beobachtungen werden nicht pauschal als bestandene Qualitätsprüfung ausgegeben.

Eigene Erstprompts, neue Testfragen und persönliche Beobachtungen werden durch technische Prüfungen nicht ersetzt.

Zwischenstand der Umstellung: Notebook01 und03 liefen mit tatsächlichen BFH-Anfragen durch. Notebook01 meldete Tokenverbrauch; Notebook03 beantwortete Bitcoin und Open Banking mit den erwarteten Quellen und den aktuellen Kurs als unbelegt. Der erste Lauf von02 zeigte einen Formatfehler im zusätzlichen JSON-Schema. Nach Vereinfachung auf Textantworten lief02 vollständig durch. Ein Schemafehler im RAG-Werkzeug von04 führte zur geprüften Umstellung auf die native BFH-Schemaausgabe; der erneute Lauf wird separat bewertet.


## Abgeschlossener BFH Durchlauf am 8 November 2026

Alle vier Notebooks wurden nach den genannten Korrekturen jeweils vollständig in einem frischen Kernel ausgeführt. Notebook01: 24 Codezellen, Notebook02: 27, Notebook03: 32, Notebook04: 20. Alle Modellantworten und Embeddings stammen aus echten BFH-Anfragen. Die Rohtexte sind in den gespeicherten Notebookausgaben dokumentiert.

Die fünf Agentenfälle verwendeten das erwartete Werkzeug und erfüllten das einfache Wortkriterium. Die drei belegbaren Dokumentfragen nannten die erwarteten Quellen; die Rechnung lieferte 90 Stunden unter der angegebenen Planungsannahme. Beim aktuellen Bitcoin-Kurs wurde Nichtwissen ausgedrückt, aber die verlangte Quellenzeichenfolge nicht exakt übernommen; quelle_ok bleibt deshalb False. Die Evaluationstabelle wird nicht nachträglich passend gemacht. Die Folgefrage erhielt mit Verlauf die Bitcoin-Antwort und ohne Bezug eine Rückfrage.

Der Memory-Vergleich zeigt weiterhin eine inhaltliche Grenze: Window verwechselt den gesuchten Antwortformat-Wunsch mit einer Sachfrage. Summary erhält den Wunsch nach zwei Stichpunkten; Buffer enthält ihn ebenfalls, nennt zusätzlich aber eine Sachfrage. Eine technisch erfolgreiche Ausführung ist somit keine vollständig bestandene Qualitätsprüfung.

Die sechs lokalen Tests bestanden. Der abschliessende Repository-Scan fand keine entfernte Betriebsart, keine vorbereiteten Modellantworten und keine zugehörige Umschaltvariable. Alte Arbeitsstände wurden ausserhalb des Repositorys gesichert. Die aktuellen Notebookausgaben wurden erst nach tatsächlicher BFH-Ausführung gespeichert.


## Einfachere Sprache und sichtbare Code Schritte

Am 8. November wurden alle erklärenden Markdownzellen der vier Notebooks überarbeitet. Lange Sätze wurden geteilt. Begriffe werden direkt am Beispiel erklärt. Kompakte Schleifen, verkürzte Entscheidungen und unbenannte Testeinträge wurden durch sichtbare Schritte ersetzt. Die gemeinsame Hilfsdatei erklärt ihre Funktionen und setzt Texte und Quellen in einzelnen Schritten zusammen. Die separate Lernhilfe enthält 28 kurze Stationen mit aufklappbaren Erklärungen.

Alle vier überarbeiteten Notebooks liefen danach erneut in frischen Kerneln mit echten BFH-Anfragen durch. Die Vektorgrafik wurde visuell geprüft. Die sechs lokalen Tests bestanden; die acht Pflichtabschnitte und die leeren Übungszellen bleiben erhalten. Es gibt weiterhin keine künstlichen Modellantworten.

Die präzisierte Vergleichsfrage in Notebook02 fragt ausdrücklich nach der Antwortform. Im aktuellen BFH-Lauf nannten Buffer und Summary korrekt zwei Stichpunkte. Window erkannte, dass im sichtbaren Ausschnitt keine ausdrückliche Vorgabe zur Antwortform stand. Diese Einzelbeobachtung ersetzt keine allgemeine Zuverlässigkeitsprüfung.

In Notebook04 nutzten die fünf Bewertungsfälle das vorgesehene Werkzeug. Das exakte Quellenkriterium für die unbeantwortbare Kursfrage blieb negativ: Das Modell sagte, dass der Kurs nicht enthalten sei, übernahm aber die verlangte Quellenzeichenfolge nicht. Die tatsächliche Ausgabe bleibt gespeichert; die Bewertung wird nicht passend gemacht.


## Ablaufgrafiken und weiter aufgeteilte Schritte in03und04

Am 8. November wurden zwei SVG-Ablaufgrafiken direkt in die Konzeptabschnitte eingebunden.03 zeigt Vorbereitung und Beantwortung getrennt;04 zeigt Suche, Rechner und Rückfrage. Die Bilddateien liegen unter notebooks/abbildungen. Beide Grafiken wurden visuell geprüft. Der Notebook-HTML-Export konnte die relativen Bildpfade auflösen und die SVGs einbetten.

In03 sind das Einstellen und Ausführen des Splitters sowie das Vorbereiten und Speichern der Chroma-Daten auf getrennte erklärte Zellen verteilt. In04 sind Agentenentscheidung und Executor getrennt. Die Rechenfunktion verwendet einen benannten Zwischenwert; Frage und Konfiguration werden vor dem Aufruf einzeln angelegt. Ein bereits ausgeführter Rechenfall erklärt die anschliessende systematische Bewertung.

Die geforderten Konzepte einschliesslich RetrievalQA, Vektorgrafik, ReAct und AgentExecutor bleiben enthalten. Es wurden keine zusätzlichen Modellaufrufe in die Lernschritte eingebaut. Die sechs lokalen Tests bestanden;03 und04 liefen danach jeweils mit echten BFH-Anfragen in frischen Kerneln durch. Die gespeicherten Antworten bleiben Einzelbeobachtungen und kein allgemeiner Qualitätsnachweis.

