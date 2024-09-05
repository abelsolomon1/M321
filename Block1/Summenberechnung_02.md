# ![](C:\Users\Abel%20Solomon%20(Schule\OneDrive%20-%20Kt.%20SG%20BLD\Fächer\Module\M321\Block1\m321_doku_as\docs\img\KSB_logo.svg)



### Projekt 1 - Summenberechnung aus Praxis Schnittstellen

#### Einleitung

In diesem Projekt setzen Sie einen einfachen Webdienst zur Summenberechnung um, der mit der Flask-Bibliothek in Python implementiert wurde. Der Dienst empfängt zwei Zahlen als Parameter über eine URL und gibt deren Summe sowie einen Namen als JSON-Objekt zurück.

#### Abgaben

1. **.py-Datei Ihres Dienstes:**

```python
from flask import Flask, request, jsonify



app = Flask(__name__)



@app.route('/summe', methods=['GET'])

def summe():

    # Abfrage der Parameter "zahl1" und "zahl2" aus der URL

    zahl1 = request.args.get('zahl1', type=float)

    zahl2 = request.args.get('zahl2', type=float)



    # Abel Solomon als Name setzen.

    name = request.args.get('name', default="Abel Solomon", type=str)



    # Überprüfen, ob die Zahlenparameter vorhanden sind

    if zahl1 is None oder zahl2 is None:

        return jsonify({"error": "Fehlende Parameter zahl1 oder zahl2"}), 400



    # Berechnung der Summe

    result = zahl1 + zahl2



    # Rückgabe der Summe und des Namens als JSON-Objekt

    return jsonify({"name": name, "summe": result})



if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000)
```

### Beantwortung von Fragen

#### **Was wird in Python mit `__name__` und `__main__` gesteuert?**

 `__name__` ist eine spezielle Variable in Python, die den Namen des aktuellen Moduls enthält. Wenn ein Skript direkt ausgeführt wird, wird `__name__` auf `'__main__'` gesetzt. Dadurch können Sie steuern, ob ein Codeblock nur ausgeführt wird, wenn das Skript direkt gestartet wird, und nicht, wenn es als Modul importiert wird. Dies wird oft verwendet, um die Ausführung des Skriptes zu initiieren, wie z.B. beim Start eines Flask-Servers.

#### **Wie ist Ihr JSON-Objekt aufgebaut? Wie könnten Sie es um weitere Parameter ergänzen?**

!!! tip "Hinweis"

Das JSON-Objekt, das von der Anwendung zurückgegeben wird, hat die folgende Struktur:

```perl
```json

{

    "name": "Abel Solomon",

    "summe": 15.5

}
```

Es enthält zwei Schlüssel: `name`, der den Namen des Benutzers oder einen Standardnamen enthält,

und `summe`, die das Ergebnis der Summenberechnung enthält. Um das JSON-Objekt um weitere

Parameter zu ergänzen, könnten Sie beispielsweise eine Multiplikation oder eine zusätzliche

Berechnung hinzufügen:

```json
{

    "name": "Abel Solomon",

    "summe": 15.5,

    "multiplikation": 42.0

}
```

```
- #### **Begrifflichkeiten klären**

  - **Was ist eine API?**

    !!! abstract "API Definition"

    Eine API (Application Programming Interface) ist eine Schnittstelle, die es ermöglicht, dass verschiedene Softwarekomponenten miteinander kommunizieren können. Sie definiert Methoden und Datenstrukturen, die von einer Softwarekomponente bereitgestellt werden, um eine bestimmte Funktionalität für andere Softwarekomponenten bereitzustellen.

  - **Wozu eine Schnittstellendeklaration?**

    !!! info "Schnittstellendeklaration"

    Eine Schnittstellendeklaration legt fest, wie die Kommunikation zwischen zwei Softwarekomponenten über eine API erfolgen soll. Sie definiert die erwarteten Eingaben, die unterstützten Aktionen und die Form der Ausgabe. Eine klare Schnittstellendeklaration ist entscheidend, um sicherzustellen, dass alle Beteiligten die API korrekt nutzen und verstehen können.

- ### Dokumentierter Zugriff auf Ihren Dienst von einem anderen Knoten des VS

  - **Screenshot und Erklärung:**

    ![Beispielbild](C:\Users\Abel%20Solomon%20(Schule\OneDrive%20-%20Kt.%20SG%20BLD\Fächer\Module\M321\Block1\m321_doku_as\docs\img\raspi_screen.jpeg)

  *Abbildung: Zugriff auf den Flask-Dienst von einem anderen Knoten aus.*

  ```perl

    Ich habe auf den Dienst zugegriffen, indem ich den folgenden Befehl auf einem anderen Rechner im selben Netzwerk ausgeführt habe:

    ```bash

    curl http://<IP-Adresse>:5000/summe?zahl1=10&zahl2=20

    ```

    Der Dienst hat korrekt die Summe zurückgegeben.

  ```

### Zugriff auf Dienst eines Mitschülers

- **Screenshot und Erklärung:**

   ![Beispielbild](C:\Users\Abel%20Solomon%20(Schule\OneDrive%20-%20Kt.%20SG%20BLD\Fächer\Module\M321\Block1\m321_doku_as\docs\img\laptop_screen.png)

*Abbildung: Zugriff auf den Dienst eines Mitschülers.*

Um auf den Dienst eines Mitschülers zuzugreifen, habe ich die IP-Adresse des entsprechenden Computers verwendet, auf dem der Flask-Dienst läuft. Der Befehl, den ich verwendet habe, ist wie folgt:

```bash
curl http://<IP-Adresse>:5000/summe?zahl1=10&zahl2=20
```

Dieser Befehl sendet eine HTTP GET-Anfrage an die angegebene URL und überträgt die Zahlen 10 und 20 als Parameter. Der Dienst auf dem Computer des Mitschülers verarbeitet diese Anfrage und gibt das Ergebnis der Summenberechnung zurück.

Der Screenshot zeigt das Ergebnis der Anfrage und bestätigt, dass der Zugriff auf den Dienst erfolgreich war. Dies zeigt, dass der Dienst ordnungsgemäß funktioniert und von anderen Geräten im Netzwerk erreichbar ist.

### Weitere Anmerkungen

- **Admonitions:** Verwenden Sie Admonitions (Hinweise) zur Hervorhebung wichtiger Informationen.

- **Code Blocks:** Nutzen Sie nummerierte Code-Blöcke, um Ihren Code übersichtlicher zu gestalten.

- **Screenshots:** Screenshots können verwendet werden, um den Prozess der Implementierung und des Zugriffs auf den Dienst visuell darzustellen.
