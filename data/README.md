# Unterlagen im Projekt

## Wissensbasis des Modul Assistenten

Die beiden unverändert übernommenen Kursunterlagen liegen unter `data/modulunterlagen`:

- `Eigenschaften-Bitcoin.pdf`: eine Seite; Eigenschaften, Transaktionen und Aufbewahrung.
- `Open Banking_Zusammenfassung.pdf`: vier Seiten; APIs, Bankrollen und Datenaustausch.

Notebook 01 liest die erste Seite der Bitcoin-Unterlage direkt. Die RAG-Pipeline in Notebook 03
und 04 indexiert ausschliesslich die zwei PDFs aus diesem Unterordner. Die Aufgaben-PDFs im
übergeordneten Ordner dienen weiterhin als Projektvorgaben und werden nicht als Fachquellen indexiert.
Dateinamen und Seitenzahlen bleiben für die Quellenangaben erhalten.

Die Open-Banking-PDF enthält auf Seite 3 auch Grafiken. Deren Beschriftungen werden beim
einfachen Textauslesen teilweise nicht erfasst. Die Beispiele verwenden den auslesbaren Text.
Antworten geben den Inhalt der bereitgestellten Unterlagen wieder; eine Prüfung auf aktuelle
Marktdaten oder inzwischen geänderte Regeln ist nicht Bestandteil des lokalen Demo-Modus.

## Identifikation der Originaldateien

SHA256:

- `Eigenschaften-Bitcoin.pdf`: `8499ffdd5253dc84bbc537d754c1d8ea0954c27fae290996e5961f7a2b70c2c2`
- `Open Banking_Zusammenfassung.pdf`: `24cf4368725f7e7db93cac0ee25deff5896a4fc5d1316bc3e4f3d9fb2ceacdf5`
