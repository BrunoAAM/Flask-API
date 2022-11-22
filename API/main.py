from flask import Flask, make_response, jsonify, request

from API.bd import Cliente

app = Flask(__name__)

@app.route('/cliente', methods=['GET'])
def get_cliente():
    return make_response(
        jsonify(Cliente)
    )

@app.route('/cliente/<int:id>', methods=['GET'])
def get_cliente_id(id):
    for cliente in Cliente:
        if cliente.get('id') == id:
            return jsonify(cliente)

@app.route('/cliente', methods=['POST'])
def create_cliente():
    cliente = request.json
    Cliente.append(cliente)
    return cliente

@app.route('/cliente/<int:id>', methods=['PUT'])
def change_cliente(id):
    changed_cliente = request.get_json()
    for indice, cliente in enumerate(Cliente):
        if cliente.get('id') == id:
            Cliente[indice].update(changed_cliente)
            return jsonify(Cliente[indice])


@app.route('/cliente/<int:id>', methods=['DELETE'])
def delete_cliente(id):
    for indice, cliente in enumerate(Cliente):
        if cliente.get('id') == id:
            del Cliente[indice]
            return jsonify(Cliente)

app.run(port=5000, host='localhost')