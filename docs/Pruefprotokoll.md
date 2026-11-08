# Prüfprotokoll

Stand 30. Oktober 2026. Geprüft mit Python 3.12 unter Windows.
Die genauen installierten Paketversionen stehen in requirements.txt.

## Tatsächlich durchgeführte Prüfungen

Alle vier Notebooks wurden mit nbclient jeweils in einem frischen Jupyter-Kernel ausgeführt.
Notebook 03 und 04 wurden nach der letzten Änderung erneut ausgeführt. Kein unerwarteter
Zellfehler blieb übrig. Erwartete Fehler werden in den Notebooks mit dem konkreten Fehlertyp
abgefangen und erläutert. Die leeren Übungszellen bleiben absichtlich unausgefüllt.

Die abschliessende Testsuite meldete **6 Tests erfolgreich**:

1. Verbindliche Notebookabschnitte, Erklärung direkt vor jeder Codezelle und leere Übungszelle.
2. Zwei echte PDF-Dateien mit erhaltenen Dateinamen und positiven Seitennummern.
3. Richtige Quellen für Anzahl Notebooks, Umfang der Reflexion und Fehlerbeispiele.
4. Nichtwissen für eine nicht belegte Frage sowie ein erklärender Fehler bei unbekannten Demo-Fällen.
5. Zulässiger und unzulässiger Eingabewert für das Tool.
6. Tatsächlich ausgeführter Toolschritt im bekannten Demo-Agentenablauf.

Die PCA-Grafik ist im dritten Notebook als PNG eingebettet und wurde auf lesbare Beschriftung
und vollständige Darstellung geprüft. Notebookausgaben enthalten keine API-Schlüssel.

## Mini Evaluation

Die fünf Fälle in ergebnisse/demo_evaluation.csv wurden ausgeführt. Die einfachen Antwortsignale
stimmen in allen fünf Fällen. Die drei Dokumentfälle verweisen auf die erwarteten Seiten 1, 4
und 2 der LangChain-Aufgabenstellung. Die unbeantwortbare Frage erhält keine Quelle. Der Rechenfall
führt das Tool aus und liefert den Planungswert 90 Stunden. Die Formulierungen stammen aus
selbst geschriebenen Testwerten; sie sind keine aufgezeichneten BFH-Antworten.

## Korrekturen aus der Prüfung

Der klassische ReAct-Parser übergibt Action Input zunächst als Text. Der Lernzeitrechner wandelt
den Wert deshalb ausdrücklich in float um. Das ist wichtig, obwohl das Tool eine numerische
Typangabe besitzt. Die erste lokale Wortsuche gewichtete häufige deutsche Wörter zu stark.
Eine kleine Stopwortliste verbesserte die bekannten Testfragen. Dies ist eine Anpassung an die
Demo-Fälle und kein Nachweis allgemeiner Suchqualität.

## Nicht geprüft

Es wurden keine Anfragen an die BFH-Inference-API gesendet, da kein persönlicher Schlüssel
vorlag. Reale Antwortqualität, Streaming-Nutzungsdaten, semantische Retrievalqualität und
autonome BFH-Toolwahl bleiben offen. Der bereitgestellte Verbindungstest und die Live-Ausführung
der Notebooks ermöglichen diese Ergänzung. Der vorbereitete GitHub-Workflow wurde lokal
entsprechend ausgeführt, aber noch nicht auf GitHub gestartet.

Die Installation erfolgte in einer getrennten Projektumgebung; die Pakete wurden nicht in die
vorhandene Benutzerumgebung installiert. Die Windows-Startdatei wurde inhaltlich geprüft, aber
nicht interaktiv per Doppelklick getestet. macOS und Linux wurden nicht getestet.

## Nachprüfung mit Python 3.13

Am 4. November 2026 wurde das Projekt auf demselben Windows-Rechner zusätzlich mit
Python 3.13.15 in einer neuen virtuellen Umgebung `.venv` geprüft.
Die zuvor festgehaltenen Paketversionen konnten unverändert installiert werden.
`pip check` meldete keine widersprüchlichen Abhängigkeiten. Alle sechs Tests bestanden.
Anschliessend liefen alle vier Notebooks jeweils in einem frischen Kernel erfolgreich durch;
insgesamt wurden 32 nicht leere Codezellen ausgeführt. Die gespeicherten Notebookausgaben
und die Demo-CSV stammen jetzt aus diesem Python-3.13-Durchlauf.

Die Versionsgrenzen im Projekt und in den Setup-Zellen erlauben nun Python 3.12 und 3.13.
Die Startanleitungen verwenden Python 3.13; der vorbereitete GitHub-Workflow prüft beide
Versionsreihen. Der geänderte Workflow wurde noch nicht auf GitHub ausgeführt.
Der lokale Durchlauf verwendete ausschliesslich den Demo-Modus und sendete keine BFH-Anfragen.
Diese technische Prüfung wurde bei der Projektvorbereitung ausgeführt und ersetzt keine eigenen
Lernversuche oder persönliche Reflexion.

## Überarbeitung des ersten Notebooks

Am 4. November 2026 wurde Notebook 01 nach einer Rückmeldung zur Verständlichkeit
und zur Ich-Form vollständig überarbeitet. Die neue Fassung verwendet allgemeine
Erklärungen, eine Leitfrage und kleinere Experimentschritte. Das Beispiel behandelt
die Bedeutung von Literate Programming anhand eines Textes aus der Aufgabenstellung.
Die bisher versehentlich als Codeblock dargestellten Absätze sind korrigiert.

Die überarbeitete Fassung lief in einem frischen Python-3.13-Kernel im Demo-Modus
erfolgreich durch (15 nicht leere Codezellen). Anschliessend bestanden alle sechs
Projektprüfungen. Es wurden keine BFH-Anfragen ausgeführt. Die anderen drei Notebooks
wurden bei dieser Überarbeitung nicht verändert.

## Umstellung auf die ausgewählten Modulunterlagen

Am 4. November 2026 wurden auf Wunsch von Lina die Kursunterlagen
Eigenschaften-Bitcoin.pdf und Open Banking_Zusammenfassung.pdf unverändert in
data/modulunterlagen übernommen. Die Dateien enthalten zusammen fünf Seiten.
Die ursprünglichen Aufgaben-PDFs bleiben als Projektvorgaben in data und werden nicht indexiert.

Notebook 01 liest die erste Seite der Bitcoin-PDF mit pypdf aus. Die Frage betrifft die auf
21 Millionen begrenzte Gesamtmenge. Die Einrichtung ist auf kleine Zellen verteilt; die
längste Codezelle hat 11 nicht leere Zeilen. Erklärungen sind allgemein formuliert und
stehen direkt vor dem jeweiligen Code. Die Beispiel-Fragen in den späteren Notebooks,
Demo-Fälle, Quellenprüfungen und die Dokumentation verwenden die neue Wissensbasis.

Alle sechs Tests bestanden. Alle vier Notebooks liefen anschliessend unabhängig in frischen
Python-3.13-Kernels erfolgreich durch, insgesamt 48 nicht leere Codezellen.
Die resultierende Demo-CSV bestätigt die erwarteten Dateinamen und Seiten für Bitcoin-Menge
(Bitcoin, S. 1), Codierungsformate (Open Banking, S. 1) und Zugriffserlaubnis (Open Banking, S. 3).
Die Frage nach dem heutigen Bitcoin-Kurs hat keinen Beleg. Der Toolfall liefert weiterhin den
ausdrücklich als Planungswert bezeichneten Wert von 90 Stunden für 3 ECTS.

Die ausgeführten Tests arbeiten mit konstruierten Demo-Antworten. Es wurden keine BFH-Anfragen
gesendet und keine Live-Modellqualität gemessen. Die in den Open-Banking-Grafiken eingebetteten
Beschriftungen werden bei dieser Text-Pipeline teilweise nicht ausgelesen. Es wurde weder ein
Commit erstellt noch ein Push zu GitHub ausgeführt.

## BFH Proxy Pfad und erster erfolgreicher Chat Aufruf

Am 4. November 2026 wurde ein beim ersten echten Notebook-Aufruf gemeldeter HTTP-404-Fehler
untersucht. Die Bibliothek bezeichnet ihn als OpenAIModelNotFoundError, obwohl dieser Fehlertyp
allein nicht zwischen falschem Modellnamen und falschem API-Pfad unterscheidet.

Die authentifizierte Prüfung ergab für denselben BFH-Proxy:

- /api/v1/models: HTTP 404.
- /v1/models: HTTP 200; qwen3.8-27b ist in der Modellliste vorhanden.

Die tatsächliche lokale BFH_BASE_URL wurde deshalb auf https://inference.proxy.ti.bfh.ch/v1
korrigiert. Modellname und Schlüssel blieben unverändert. Die geprüfte Proxy-Adresse ist nun
auch der Vorgabewert im ersten Notebook, in den gemeinsamen Modellfunktionen und in der
Beispielkonfiguration. Die Dokumentation nennt teils nur den Host und verwendet in internen
Codebeispielen noch /api/v1; die Korrektur hier beruht auf der tatsächlich geprüften Proxy-Route.

Ein anschliessender echter Chat-Aufruf mit qwen3.8-27b lieferte den angeforderten Satz
«Verbindung funktioniert.». Der Dienst meldete 24 Eingabe-Tokens, 48 Ausgabe-Tokens und
72 Tokens insgesamt, davon 41 Reasoning-Tokens innerhalb der Ausgabe. Der Aufruf dauerte
etwa 4.37 Sekunden. Dies war ein technischer Verbindungstest bei der Projektvorbereitung,
kein eigener Prompt-Vergleich und keine vollständige Live-Evaluation der Bitcoin-Fragen.
Der Embedding-Aufruf wurde dabei nicht getestet.

Anschliessend bestanden alle sechs lokalen Tests im Demo-Modus. Die veralteten Ausgaben
des ersten Notebooks wurden entfernt, damit nach dem Neustart keine alten Fehler oder
Demo-Ergebnisse mit der neuen Live-Ausführung verwechselt werden. Die vorherige Fassung
des Notebooks wurde ausserhalb des Repositorys gesichert; die Schlüsseldatei wurde nicht kopiert.


## Überarbeitung der Lernnotebooks am 5 November 2026

Notebook 02 und 03 wurden in 62 beziehungsweise 72 Zellen mit einzeln erklärten
Arbeitsschritten aufgeteilt. Notebook 04 zeigt nun Toolregistrierung, ReAct-Prompt,
create_react_agent und AgentExecutor unmittelbar im Notebook. Seine Evaluation
ruft für alle fünf Fälle den vollständigen Assistenten auf; Verlauf und Folgefrage
werden zusätzlich verglichen. Die höchstens zwölf nichtleeren Codezeilen je Zelle
und die Erklärungen wurden statisch kontrolliert.

Die überarbeiteten Fassungen von 02, 03 und 04 liefen im Demo-Modus in getrennten
Kerneln durch. Die RAG-Grafik wurde als Notebook-Ausgabe gespeichert und visuell
geprüft. Acht Projekttests sind erfolgreich, darunter zusätzliche Prüfungen der
Dokumentsuche durch den Agenten und der Rückfrage bei fehlendem Bezug.

Der echte BFH-Durchlauf von 02 deckte dagegen einen Formatfehler im Window-Fall auf:
Das Modell lieferte Text mit nicht korrekt maskierten Anführungszeichen innerhalb
eines JSON-Textwerts. Der angeforderte json_object-Modus verhinderte diesen Fehler
bei einem zweiten Versuch nicht. Ein erfolgreicher Live-Durchlauf ist damit noch
nicht nachgewiesen. Die Frage wurde anschliessend präzisiert, um Nutzerwunsch und
Systemregeln ausdrücklich zu trennen; diese letzte Änderung ist noch live zu prüfen.
Der Pydantic-Parser wird nicht umgangen und es gibt keinen stillen Demo-Ersatz.

Der Reflexionsbericht beschreibt den dokumentierten Zwischenstand. Eigene
Erstprompts und die selbstständige Bearbeitung von 02 bis 04 bleiben ausdrücklich
offen. Automatische technische Prüfungen werden nicht als persönliche Erfahrungen
von Lina dargestellt. Keine Veröffentlichung auf GitHub vorgenommen.

Der Live-Durchlauf von Notebook 03 wurde vollständig ausgeführt: echte BFH-Embeddings mit 768 Dimensionen, Bitcoin-Beleg korrekt, aktueller Kurs korrekt als unbelegt behandelt. Die Open-Banking-Frage blieb trotz vorhandener Unterlage unbeantwortet; fünf Retrieval-Treffer enthielten den benötigten Tabellenabschnitt nicht. Deshalb wurde k auf acht erhöht. Die Qualitätsprüfung dieses geänderten Werts ist noch offen. Erfolgreiche Programmausführung wird nicht mit korrekten Antworten gleichgesetzt.

Die weitere BFH-Prüfung von 02 lief mit der präzisierten Frage vollständig ohne Parserfehler durch. Inhaltlich blieb ein Unterschied: Die Summary enthielt den frühen Antwortwunsch, die Antwort verweigerte dessen Verwendung wegen der strengen Formulierung zur ersten Originalnachricht. Diese Frage muss vor dem Abschluss so präzisiert werden, dass auch die ausdrücklich mitgegebene Summary als Gesprächsdaten gilt. Reine Ausführbarkeit ist hier noch kein vollständiger Lernzielnachweis.


## Abschliessender Stand am 5 November 2026

Die abschliessende Einzelprobe von Notebook 03 mit acht Treffern beantwortete beide
Fachfragen korrekt mit Quelle: Bitcoin 21 Millionen auf S.1; JSON/XML auf S.1 der
Open-Banking-Unterlage. Der aktuelle Bitcoin-Kurs wurde zutreffend als unbelegt behandelt.

Notebook 02 wurde technisch vollständig über BFH ausgeführt. Buffer und Summary
erhielten den frühen Wunsch korrekt. Window verwechselte die spätere Sachfrage
mit einem Antwortwunsch. Dieser negative Qualitätsbefund wird im Notebook erklärt.

Notebook 04 wurde vollständig über BFH ausgeführt. Alle fünf Fälle nutzten die
erwarteten Tools; die drei belegbaren Antworten enthielten die erwarteten Quellen.
Die Rechnung verwendete das Tool mit Eingabe3 und dessen Ergebnis90. Die Folgefrage
wurde mit Verlauf auf Bitcoin bezogen; die neue Sitzung ohne Bezug erhielt eine
Rückfrage. Für den heutigen Kurs verweigerte das Modell korrekt eine Kursangabe,
übernahm aber die exakte Zeichenfolge keine Quelle nicht. Deshalb bleibt das
automatische Quellenkriterium in Q4 negativ. Es ist eine Formatabweichung und
keine erfundene Sachantwort. Rohdaten: ergebnisse/bfh_pruefnachweise.json und
ergebnisse/bfh_evaluation.csv. Diese Einzelprobe beweist keine generelle Zuverlässigkeit.

Die Reflexion liegt ausformuliert und als visuell geprüfte zweiseitige PDF vor.
Die Notebooktexte verwenden eine allgemeine deutsche Darstellung. Alle neuen
Codezellen sind kurz und erklärt; eigene Logbucheinträge bleiben ehrlich offen.

Abschlussprüfung: Die finalen drei Notebooks liefen erneut jeweils in einem frischen Kernel im Offline-Modus ohne unerwartete Ausnahme. Die Strukturprüfung bestätigt alle acht Pflichtabschnitte, unmittelbar erklärte Codezellen, höchstens zwölf nichtleere Codezeilen, allgemeine deutsche Notebooktexte und eine leere Übungszelle. Die PDF-Reflexion wurde auf beiden Seiten visuell geprüft. Die offenen persönlichen Nachweise bleiben davon getrennt.

Letzter Wiederholungstest nach Korrektur des Demo-Kontextbezugs: Notebook04 erneut vollständig offline ausgeführt; alle acht Unittests erfolgreich. Der Demo-Test prüft den tatsächlichen History-Abschnitt statt Wörter in den Systemregeln. Die BFH-Logik ist von diesem Testskript getrennt.
