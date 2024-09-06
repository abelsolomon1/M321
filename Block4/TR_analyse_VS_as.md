# Verteiltes System: Taschenrechner mit Raspberry Pis und GUI-Client

## Überblick

In unserem verteilten System (VS) besteht die Berechnungslogik aus mehreren Raspberry Pis, die über das Netzwerk verbunden sind, während der Client (eine GUI) auf einem PC läuft, der außerhalb des Netzwerks liegt. Der Client übermittelt Anfragen für Berechnungen an die Raspberry Pis, die dann die Berechnung durchführen und das Ergebnis zurück an den Client senden.

### Eigenschaften eines verteilten Systems (VS)

Ein verteiltes System hat mehrere Merkmale. 

Hier ein paar Beispiele:

- Viele Prozessoren, Speicher, Subsysteme,...
- Kopplung autonomer Verarbeitungsknoten durch ein Kommunikationsmedium
- Kommunikation zwischen den Knoten erfolgt nur über Nachrichtenaustausch
- Knoten des VS verfolgen gemeinsames Ziel, bereitgestellte Leistung wird durch arbeitsteilige Kooperation erbracht
- Kein gemeinsamer Speicher, aber gemeinsames Wissen um System(teil-)zustand
- Keine allen gemeinsame Fehlerquelle
- Unabhängiges Fehlerverhalten der Teilsysteme

 Quelle:[Allgemein - Modul 321 Verteilte Systeme programmieren](https://kantonsschuleambruehl.gitlab.io/m321/0-1/#merkmale-vor-und-nachteile-von-vs)

### Merkmale, die unser VS erfüllt, und welche nicht

| **Merkmal**                                                   | **Erfüllt unser VS (Taschenrechner)?**                                                             |
| ------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| **Zusammenschluss unabhängiger Computer**                     | Ja, die Raspberry Pis und der PC arbeiten unabhängig. Der Client sendet Anfragen an die Pis.       |
| **Physische oder virtuelle Komponenten**                      | Ja, die Raspberry Pis sind physische Geräte im Netzwerk.                                           |
| **Erscheint dem Benutzer als ein einzelnes System**           | Ja, der Benutzer sieht nur die GUI, nicht die Raspberry Pis im Hintergrund.                        |
| **Kopplung autonomer Knoten durch Nachrichtenaustausch**      | Ja, der Client sendet Berechnungen über HTTP und erhält Ergebnisse.                                |
| **Kein gemeinsamer Speicher, aber gemeinsamer Systemzustand** | Nein, die Raspberry Pis haben keinen gemeinsamen Speicher oder Systemzustand.                      |
| **Unabhängiges Fehlerverhalten der Knoten**                   | Ja, wenn ein Pi ausfällt, funktioniert das System, wenn andere verfügbar sind.                     |
| **Skalierbarkeit**                                            | Ja, man kann weitere Pis hinzufügen, um die Berechnungen zu verteilen.                             |
| **Verfügbarkeit und Reduktion der Antwortzeit**               | Nein, Netzwerklatenz und Pis-Leistung können die Antwortzeit verlangsamen.                         |
| **Transparenz (z.B. Fehlertransparenz, Ortstransparenz)**     | Nein, Fehler und Ausfälle sind für den Benutzer sichtbar. Der Standort der Pis spielt keine Rolle. |
| **Redundanz**                                                 | Nein, es gibt keine automatische Redundanz bei Ausfällen eines Pis.                                |


