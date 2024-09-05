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
    if zahl1 is None or zahl2 is None:
        return jsonify({"error": "Fehlende Parameter zahl1 oder zahl2"}), 400
    
    # Berechnung der Summe
    result = zahl1 + zahl2
    
    # Rückgabe der Summe und des Namens als JSON-Objekt
    return jsonify({"name": name, "summe": result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
