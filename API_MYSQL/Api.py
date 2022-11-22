from flask import Flask, request, make_response, jsonify
from MySQL import mydb, mycursor;

app = Flask(__name__)

@app.route('/cliente', methods=['GET'])
def get_cliente():
    mycursor.execute('SELECT * FROM customers')
    clientes = mycursor.fetchall()
    cliente = list()
    for meu_cliente in clientes:
        cliente.append(
            {
               'id': meu_cliente[0],
                'nome': meu_cliente[1],
                'email': meu_cliente[2],
                'cpf': meu_cliente[3],
                'cep': meu_cliente[4]
            }
        )

    return make_response(
        jsonify(cliente)
    )

@app.route('/cliente/<int:id>', methods=['GET'])
def get_cliente_id(id):
    sql = "SELECT * FROM customers WHERE id = %s"
    adr = (id,)
    mycursor.execute(sql, adr)
    clientes= mycursor.fetchall()
    cliente = list()
    for meu_cliente in clientes:
        cliente.append(
            {
                'id': meu_cliente[0],
                'nome': meu_cliente[1],
                'email': meu_cliente[2],
                'cpf': meu_cliente[3],
                'cep': meu_cliente[4]
            }
        )
    return make_response(
        jsonify(cliente)
    )

@app.route('/cliente', methods=['POST'])
def create_cliente():
    cliente = request.json
    sql = "INSERT INTO customers (name, email, cpf, cep) VALUES (%s, %s, %s, %s)"
    val = (cliente["nome"], cliente["email"], cliente["cpf"], cliente["cep"])
    mycursor.execute(sql, val)
    mydb.commit()

    return make_response(
        jsonify(cliente)
    )

@app.route('/cliente/<int:id>', methods=['PUT', 'GET'])
def change_cliente(id):
    cliente = request.get_json()
    sql = "UPDATE customers SET name = %s, email = %s, cpf = %s, cep = %s WHERE id = %s"
    val = (cliente["nome"], cliente["email"], cliente["cpf"], cliente["cep"], id,)
    mycursor.execute(sql, val)
    mydb.commit()
    sql = "SELECT * FROM customers WHERE id = %s"
    adr = (id,)
    mycursor.execute(sql, adr)
    clientes = mycursor.fetchall()
    cliente = list()
    for meu_cliente in clientes:
        cliente.append(
            {
                'id': meu_cliente[0],
                'nome': meu_cliente[1],
                'email': meu_cliente[2],
                'cpf': meu_cliente[3],
                'cep': meu_cliente[4]
            }
        )
    return make_response(
        jsonify(cliente)
    )


@app.route('/cliente/<int:id>', methods=['DELETE', 'GET'])
def delete_cliente(id):
    sql = "DELETE FROM customers WHERE id = %s"
    adr = (id,)
    mycursor.execute(sql, adr)
    mydb.commit()
    mycursor.execute('SELECT * FROM customers')
    clientes = mycursor.fetchall()
    cliente = list()
    for meu_cliente in clientes:
        cliente.append(
            {
                'id': meu_cliente[0],
                'nome': meu_cliente[1],
                'email': meu_cliente[2],
                'cpf': meu_cliente[3],
                'cep': meu_cliente[4]
            }
        )

    return make_response(
        jsonify(cliente)
    )


app.run(port=5000, host='localhost')

