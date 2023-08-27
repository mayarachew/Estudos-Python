import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='1234',
    database='db',
)

cursor = conexao.cursor()

# CRUD
# CREATE
nome_produto = "chocolate"
valor = 15

command = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})' # comando SQL
cursor.execute(command) # executando o comando SQL
conexao.commmit() # editando o banco de dados

# CRUD
comando = f'SELECT * FROM vendas'
cursor.execute(comando)
result = cursor.fetchall() # lendo o banco de dados
print(result)

# UPDATE
nome_produto = "todynho"
valor = 6

comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit() # edita o banco de dados

# DELETE
nome_produto = "todynho"

comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit()

# TODO ...

cursor.close()
conexao.close()
