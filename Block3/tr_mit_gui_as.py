import tkinter as tk
import requests

# Funktion, um das Ergebnis vom Server zu bekommen
def get_result(operation, zahl1, zahl2):
    base_url = 'http://localhost:5000'  # Lokale IP-Adresse und Port
    urls = {
        'addieren': '/add',
        'subtrahieren': '/sub',
        'multiplizieren': '/mul',
        'dividieren': '/div'
    }
    
    url = base_url + urls.get(operation, '/add')
    params = {'zahl1': zahl1, 'zahl2': zahl2}
    
    try:
        # Testen, ob der Server erreichbar ist
        response = requests.get(url, params=params)
        response.raise_for_status()
        
        # Server hat Antwort gesendet:
        result = response.json()
        return result.get('result', 'Fehler beim Abrufen des Ergebnisses')
    
    except requests.exceptions.ConnectionError:
        return "Server ist nicht erreichbar. Bitte sicherstellen, dass der Server läuft."
    except requests.exceptions.HTTPError as errh:
        return f"HTTP-Fehler: {errh}"
    except requests.exceptions.Timeout as errt:
        return f"Timeout-Fehler: {errt}"
    except requests.exceptions.RequestException as err:
        return f"Fehler: {err}"

# Funktionen für die Berechnungen
def addieren():
    try:
        zahl1 = float(entry_1.get())
        zahl2 = float(entry_2.get())
        result = get_result('addieren', zahl1, zahl2)
        solution_entry.delete(0, tk.END)  # Vorherigen Text löschen
        solution_entry.insert(0, f"{result}")
    except ValueError:
        solution_entry.delete(0, tk.END)
        solution_entry.insert(0, "Ungültige Eingabe. Bitte Zahlen eingeben.")

def subtrahieren():
    try:
        zahl1 = float(entry_1.get())
        zahl2 = float(entry_2.get())
        result = get_result('subtrahieren', zahl1, zahl2)
        solution_entry.delete(0, tk.END)
        solution_entry.insert(0, f"{result}")
    except ValueError:
        solution_entry.delete(0, tk.END)
        solution_entry.insert(0, "Ungültige Eingabe. Bitte Zahlen eingeben.")

def multiplizieren():
    try:
        zahl1 = float(entry_1.get())
        zahl2 = float(entry_2.get())
        result = get_result('multiplizieren', zahl1, zahl2)
        solution_entry.delete(0, tk.END)
        solution_entry.insert(0, f"{result}")
    except ValueError:
        solution_entry.delete(0, tk.END)
        solution_entry.insert(0, "Ungültige Eingabe. Bitte Zahlen eingeben.")

def dividieren():
    try:
        zahl1 = float(entry_1.get())
        zahl2 = float(entry_2.get())
        result = get_result('dividieren', zahl1, zahl2)
        solution_entry.delete(0, tk.END)
        solution_entry.insert(0, f"{result}")
    except ValueError:
        solution_entry.delete(0, tk.END)
        solution_entry.insert(0, "Ungültige Eingabe. Bitte Zahlen eingeben.")

# GUI Setup
root = tk.Tk()
root.title("Einfacher Taschenrechner")

# Eingabefelder
tk.Label(root, text="Erste Zahl:").grid(row=0, column=0)
entry_1 = tk.Entry(root)
entry_1.grid(row=0, column=1)

tk.Label(root, text="Zweite Zahl:").grid(row=1, column=0)
entry_2 = tk.Entry(root)
entry_2.grid(row=1, column=1)

# Ergebnis Label und Solution-Feld
tk.Label(root, text="Solution:").grid(row=2, column=0)
solution_entry = tk.Entry(root)
solution_entry.grid(row=2, column=1)

# Buttons für Operationen
tk.Button(root, text="+", command=addieren).grid(row=3, column=0)
tk.Button(root, text="-", command=subtrahieren).grid(row=3, column=1)
tk.Button(root, text="*", command=multiplizieren).grid(row=4, column=0)
tk.Button(root, text="/", command=dividieren).grid(row=4, column=1)

root.mainloop()
