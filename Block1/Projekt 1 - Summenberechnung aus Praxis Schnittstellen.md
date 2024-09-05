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

**Beantwortung von Fragen:**

**Was wird in Python mit `__name__` und `__main__` gesteuert?**  
`__name__` ist eine spezielle Variable in Python, die den Namen des aktuellen Moduls enthält. Wenn ein Skript direkt ausgeführt wird, wird `__name__` auf `'__main__'` gesetzt. Dadurch können Sie steuern, ob ein Codeblock nur ausgeführt wird, wenn das Skript direkt gestartet wird, und nicht, wenn es als Modul importiert wird. Dies wird oft verwendet, um die Ausführung des Skriptes zu initiieren, wie z.B. beim Start eines Flask-Servers.

**Wie ist Ihr JSON-Objekt aufgebaut? Wie könnten Sie es um weitere Parameter ergänzen?**  
Das JSON-Objekt, das von der Anwendung zurückgegeben wird, hat die folgende Struktur:

```python
{
    "name": "Abel Solomon",
    "summe": 15.5
}
```

Es enthält zwei Schlüssel: `name`, der den Namen des Benutzers oder einen Standardnamen enthält, und `summe`, die das Ergebnis der Summenberechnung enthält. Um das JSON-Objekt um weitere Parameter zu ergänzen, könnten Sie beispielsweise eine Multiplikation oder eine zusätzliche Berechnung hinzufügen:

```python
{
    "name": "Abel Solomon",
    "summe": 15.5,
    "multiplikation": 42.0
}
```

- **Begrifflichkeiten klären:**
  
  - **Was ist eine API?**  
    Eine API (Application Programming Interface) ist eine Schnittstelle, die es ermöglicht, dass verschiedene Softwarekomponenten miteinander kommunizieren können. Sie definiert Methoden und Datenstrukturen, die von einer Softwarekomponente bereitgestellt werden, um eine bestimmte Funktionalität für andere Softwarekomponenten bereitzustellen.
  
  - **Wozu eine Schnittstellendeklaration?**  
    Eine Schnittstellendeklaration legt fest, wie die Kommunikation zwischen zwei Softwarekomponenten über eine API erfolgen soll. Sie definiert die erwarteten Eingaben, die unterstützten Aktionen und die Form der Ausgabe. Eine klare Schnittstellendeklaration ist entscheidend, um sicherzustellen, dass alle Beteiligten die API korrekt nutzen und verstehen können.

- **Dokumentierter Zugriff auf Ihren Dienst von einem anderen Knoten des VS**
  
  - **Screenshot und Erklärung:**  
    (Fügen Sie hier einen Screenshot ein, der zeigt, wie Sie von einem anderen Rechner im Netzwerk auf Ihren Flask-Dienst zugegriffen haben. Beschreiben Sie den Prozess, wie Sie die Anfrage gesendet und die Antwort erhalten haben.)

- **Zugriff auf Dienst eines Mitschülers**
  
  - **Screenshot und Erklärung:**  
    (Fügen Sie hier einen Screenshot und eine kurze Erklärung ein, wie Sie erfolgreich auf den Dienst eines Mitschülers zugegriffen haben.)
