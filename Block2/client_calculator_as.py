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
