from flask import Flask, request, jsonify
from cliente import verificar_cliente

app = Flask(__name__)

@app.route('/cliente', methods=['POST'])
def consultar_cliente():
    data = request.get_json()

    if not data or 'ci' not in data:
        return jsonify({
            "accion": "Cliente no está en el sistema",
            "codRes": "ERROR",
            "menRes": "Error cliente",
            "ci": None
        })

    ci = str(data['ci'])
    resultado = verificar_cliente(ci)
    return jsonify(resultado)

if __name__ == '__main__':
    app.run(host='localhost', port=5003)
