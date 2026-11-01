# Einordnung der Vorlage und der E Mail

Raquels Repository wurde am 30. Oktober 2026 im Stand
b5dc4e94c2767b651470ce0fd8966a1145f92a69 gelesen. Durchgesehen wurden README, FAQ,
Konzept, die sieben Notebooks und ausgewählte Implementierungen und Tests. Das Repository wurde
hier nicht vollständig ausgeführt; Aussagen zu dessen Laufverhalten sind entsprechend keine eigenen Messungen.

Die eingefügte E-Mail enthält Raquels Einladung zur Feedbackrunde und Andrés Rückmeldung.
Die Aussage, alle sieben Notebooks ausgeführt zu haben, stammt von André. Sie ist kein Nachweis
für einen eigenen Durchlauf von Lina und wird in dieser Arbeit nicht als solcher verwendet.
Eine separate klassische Hausarbeit von Raquel war nicht dabei; die eigentliche Referenz ist ihre Notebook-Reihe.

## Was sich als Anregung eignet

Besonders hilfreich ist, dass Raquel an einem einzigen Assistenten weiterarbeitet und neue
Konzepte jeweils aus einer Grenze des bisherigen Systems ableitet. Die feste innere Struktur
erleichtert die Orientierung. Absichtliche Fehler werden als überprüfbare Lernbeispiele behandelt.
Auch die Trennung reproduzierbarer Testläufe von veränderlichen Modellantworten ist sinnvoll.

Mein Projekt setzt diese Prinzipien eigenständig für LangChain und vier deutschsprachige
Notebooks um. Ein komplexer LangGraph-Kontrollfluss mit Reducern, Schleifen und menschlicher
Freigabe wäre für diese Aufgabenstellung unnötig. Der zentrale Lernweg ist stattdessen
Nachricht und Prompt, Gesprächsverlauf, PDF-basierte Antworten und schliesslich Toolnutzung.

## Was aus Andrés Feedback konkret folgt

- Die Notebooks enthalten gespeicherte Demo-Ausgaben, damit sie bereits beim Lesen verständlich sind.
- Jeder stille Fehler wird ausdrücklich als solcher bezeichnet; ein assert kann hier den Fehler belegen.
- Übungen unterscheiden klar zwischen Demo-Codeprüfung und echtem BFH-Modellversuch.
- Unbekannte Demo-Fragen lösen eine erklärende Fehlermeldung aus, statt passende Antworten vorzutäuschen.
- setup.bat verwendet die Python-Datei der Umgebung direkt und benötigt keine PowerShell-Aktivierung.

## Grenzen der Vorlage

Raquels aufgezeichnete Modellantworten gehören zu ihrem Korpus und ihren Experimenten.
Sie sind nicht auf die vorliegenden PDFs oder ein BFH-Modell übertragbar. Deshalb enthält dieses
Projekt eigene, ausdrücklich konstruierte Testwerte. Erfolgreiche Tests sagen nur etwas über
die bekannten Abläufe aus. Die didaktische Verständlichkeit erfordert weiterhin Rückmeldung
von Leserinnen und Lesern mit Python-Grundkenntnissen.

Quelle: https://github.com/RaquelKehl/learn-langgraph-literate-notebooks
