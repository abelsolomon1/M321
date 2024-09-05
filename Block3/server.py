from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add')
def addieren():
    zahl1 = float(request.args.get('zahl1'))
    zahl2 = float(request.args.get('zahl2'))
    result = zahl1 + zahl2
    return jsonify({'result': result})

@app.route('/sub')
def subtrahieren():
    zahl1 = float(request.args.get('zahl1'))
    zahl2 = float(request.args.get('zahl2'))
    result = zahl1 - zahl2
    return jsonify({'result': result})

@app.route('/mul')
def multiplizieren():
    zahl1 = float(request.args.get('zahl1'))
    zahl2 = float(request.args.get('zahl2'))
    result = zahl1 * zahl2
    return jsonify({'result': result})

@app.route('/div')
def dividieren():
    zahl1 = float(request.args.get('zahl1'))
    zahl2 = float(request.args.get('zahl2'))
    if zahl2 != 0:
        result = zahl1 / zahl2
    else:
        result = 'Division durch 0 ist nicht erlaubt'
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
