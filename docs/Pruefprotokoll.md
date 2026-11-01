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

Die eigene Prompt-Historie und die persönliche Abschlussreflexion sind keine technischen
Prüfergebnisse und müssen von Lina selbst ergänzt werden. Die Vorlage von Raquel wurde gelesen,
aber nicht als vollständige Notebook-Reihe ausgeführt.
