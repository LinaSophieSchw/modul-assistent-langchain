# Abschlussreflexion zum Modul Assistenten

Diese Datei enthält eine Gliederung für die persönliche Reflexion im geforderten Umfang von
etwa ein bis zwei Seiten. Die Antworten müssen meine tatsächliche Arbeit beschreiben.
Die technischen Feststellungen unten sind Ausgangspunkte, keine behaupteten eigenen Erfahrungen.

## Technisches Verständnis

Technischer Ausgangspunkt: Ein LLM-Aufruf ist zustandslos. Memory entsteht durch das erneute
Mitsenden von Nachrichten, RAG durch die Suche in externen Unterlagen. Ein Ausgabeparser
prüft die Struktur, aber nicht automatisch den Wahrheitsgehalt.

Meine Ergänzung: Welchen dieser Punkte habe ich zuerst anders verstanden? Welche konkrete
Zelle oder welcher beobachtete Fehler hat meine Erklärung verändert? Was würde ich einer
anderen Studentin heute dazu sagen? Hier etwa zwei bis drei Absätze aus eigener Erfahrung ergänzen.

## Zusammenarbeit mit der KI

Für jedes Notebook ergänze ich meinen tatsächlich selbst formulierten Erstprompt und den
Vergleich mit der vorgeschlagenen Endversion. Ein bereits vorliegender KI-Vorschlag kann nicht
nachträglich als mein unbeeinflusster Erstprompt gelten. Für einen sauberen eigenen Versuch
formuliere ich zu einer neuen, vergleichbaren Frage zuerst selbst einen Prompt.

Meine Ergänzung: Welche Fragen habe ich der KI gestellt? Welche Vorschläge habe ich geprüft,
geändert oder verworfen? Wo blieb die Antwort trotz genauerer Anweisung falsch oder unklar?
Mindestens ein konkretes Beispiel mit Modell und Datum beschreiben.

## Herausforderungen

Technischer Ausgangspunkt: Paketversionen, PDF-Extraktion, die Auswahl passender Chunks
und eine valide ReAct-Antwort sind unterschiedliche Fehlerquellen. Der lokale Modus kann die
Programmlogik prüfen; er kann keine zuverlässigen BFH-Modellantworten garantieren.

Meine Ergänzung: Was war bei meinem eigenen Durchlauf am schwierigsten? Welche Fehlermeldung
trat tatsächlich auf? Wie habe ich die Ursache eingegrenzt? Was würde ich beim nächsten Mal
früher testen? Hier ein tatsächlich aufgetretenes Problem und seine Lösung beschreiben.

## Entwicklung des Modul Assistenten

Technischer Ausgangspunkt: Das fertige Beispiel ist ein kleiner, überprüfbarer Lernassistent
über zwei Projektunterlagen. Die feste RAG-Chain beantwortet Dokumentfragen; ein Agent ergänzt
die Auswahl zwischen Suche und Rechentool. Mehr Autonomie bedeutet zusätzlichen Prüfbedarf.

Meine Ergänzung: Wie sah meine erste Vorstellung aus? Welche Funktion war am Ende wichtiger
als erwartet? Welche Einschränkung würde ich einer Nutzerin ausdrücklich erklären? Mit Bezug
auf die eigenen Ergebnisse aus Notebook 04 abschliessen.

## Zwei mögliche Erweiterungen

**Bessere Suche bei Anschlussfragen.** Der Assistent könnte Fragen wie «Und wie lang soll sie sein?»
vor der Suche mit Hilfe des bisherigen Verlaufs in eine eigenständige Frage umformulieren.
Das verbindet Notebook 02 und 03 auch bei mehrdeutigen Folgefragen und liesse sich an passenden
Gesprächspaaren gegen die bisherige direkte Suche vergleichen.

**Systematische Prüfung der Belegtreue.** Ein grösserer, vorab beschrifteter Fragensatz könnte
Antwortbarkeit, Sollseiten und wichtige Aussagen festhalten. Mehrere BFH-Durchläufe pro Frage
würden sichtbar machen, welche Fehler durch Retrieval und welche durch Formulierung entstehen,
statt die Qualität allein an wenigen passenden Beispielantworten zu beurteilen.

## Vorschlag zur Offenlegung der KI Unterstützung

Die erste technische Projektfassung und Formulierungsvorschläge wurden mit Codex erstellt.
Eigene Änderungen, durchgeführte Modellversuche und manuelle Prüfungen ergänze ich hier konkret:
[Von mir tatsächlich ausgeführte Tätigkeiten eintragen.] Die persönliche Reflexion und die
Erstprompts beschreiben meine eigenen Arbeitsschritte. Vorgaben der Hochschule zur Offenlegung
und zulässigen Nutzung von KI sind zusätzlich zu beachten.
