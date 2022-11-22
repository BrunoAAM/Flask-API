import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Sql.2022+",
  database="Store"
)

mycursor = mydb.cursor()

# Criação do Banco de Dados
# mycursor.execute("CREATE DATABASE Store")
# mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), email VARCHAR(255), cpf VARCHAR(11), cep(8))")
