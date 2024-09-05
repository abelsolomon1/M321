# Dokumentation des Clients

## Client-Code

Der folgende Python-Client sendet zwei Zahlen an den Webdienst und gibt die Antwort in der Konsole aus.

```python
import requests

def get_summe(zahl1, zahl2):
    url = "http://localhost:5000/summe"
    params = {"zahl1": zahl1, "zahl2": zahl2}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        print(f"Name: {data['name']}")
        print(f"Summe: {data['summe']}")
    else:
        print("Fehler beim Zugriff auf den Dienst:", response.status_code)

if __name__ == "__main__":
    zahl1 = float(input("Geben Sie die erste Zahl ein: "))
    zahl2 = float(input("Geben Sie die zweite Zahl ein: "))
    get_summe(zahl1, zahl2)
```

## Erklärung der Konsolenausgabe

1. **Führen Sie das Client-Skript aus:**
   
   Geben Sie folgenden Befehl in der Konsole ein:
   
   ```bash
   python client_calculator_as.py
   ```

Konsoleneingabe:

```bash
Geben Sie die erste Zahl ein: 15
Geben Sie die zweite Zahl ein: 20
```

Erwartete Konsolenausgabe:

```bash
Name: Abel Solomon
Summe: 35.0
```

**Screenshot:**

![Client Konsolenausgabe](C:\Users\Abel%20Solomon%20(Schule\OneDrive%20-%20Kt.%20SG%20BLD\Fächer\Module\M321\Block2\img\screenshot_konsolenausgabe.png)

**Erklärung:**

- **Eingabeaufforderung:** Der Client fordert den Benutzer auf, zwei Zahlen einzugeben.
- **Ausgabe:** Nach der Eingabe der Zahlen wird die Summe zusammen mit dem Namen "Abel Solomon" vom Webdienst zurückgegeben und auf der Konsole angezeigt.

## Fazit

Dieser Client ermöglicht es Benutzern, mit dem Webdienst zur Summenberechnung zu interagieren. Er fordert die Eingabe von zwei Zahlen an, sendet diese an den Dienst, und zeigt das Ergebnis der Berechnung zusammen mit dem Namen des Benutzers auf der Konsole an.
