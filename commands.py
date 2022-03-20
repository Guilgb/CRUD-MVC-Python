import mysql.connector

# ------------------------Conetando com BD ------------------------
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="crud2"
)

cursor = db.cursor()
# ------------------------ Criando BD ------------------------
# cursor.execute("CREATE DATABASE crud")


# ------------------------ Verificando o BD ------------------------
# cursor.execute("SHOW DATABASES")

# for x in cursor:
#     print(x)


# ------------------------ Criando Tabelas ------------------------
# cursor.execute("CREATE TABLE pessoa(nome VARCHAR(255) PRIMARY KEY)")


# ---------------------- Verificando se a tabela existe ----------------------
# cursor.execute("SHOW TABLES")
# for x in cursor:
#     print(x)


# ------------------------ Inserindo coluna na tabela ------------------------
# cursor.execute("ALTER TABLE pessoa ADD telefones VARCHAR(11)")


# ------------------------Inserir dados na Tabela ------------------------
# sql = "INSERT INTO pessoa (nome, telefones) VALUES(%s, %s)"
# val = ('Gael', '88766546545')
# cursor.execute(sql, val)
# db.commit()
# print(cursor.rowcount, "record inserted.")

# ------------------------ Selencionar dados da tabela ------------------------

# cursor.execute("SELECT * FROM pessoa")
# result = cursor.fetchall()

# for i in result:
#     print(i)

# ------------------------ Selencionar dados da Coluna ------------------------
# cursor.execute("SELECT nome FROM pessoa")
# result = cursor.fetchall()

# for i in result:
#     print(i)


# ------------------------ Selencionar apenas um Dado ------------------------
# escolaridade = "Nenhuma"


# def idCidade():
#     cursor.execute(f"SELECT idEscolaridade FROM Escolaridade where nomeEscolaridade= '{escolaridade}'"
#                    )
#     result = cursor.fetchall()
#     print(result)


# ------------------------ Selencionar apenas um Dado ------------------------
cursor.execute("SELECT * FROM Instrutor WHERE nomeInstrutor = 'Guilherme'")
result = cursor.fetchall()
for i in result:
    print(i)


# ------------------------ Ordenação Crescente ------------------------

# sql = "SELECT * FROM pessoa ORDER BY nome"
# cursor.execute(sql)
# result = cursor.fetchall()
# for i in result:
#     print(i)

# ------------------------ Ordenação decrescente ------------------------

# sql = "SELECT * FROM pessoa ORDER BY nome DESC"
# cursor.execute(sql)
# result = cursor.fetchall()
# for i in result:
#     print(i)

# ------------------------ Apagar registro ------------------------

# sql = "DELETE FROM pessoa WHERE nome = 'Gael'"
# cursor.execute(sql)
# db.commit()

# print(cursor.rowcount, "record(s) deleted")

# ------------------------ Apagar registro pt.2 ------------------------

# sql = "DELETE FROM pessoa WHERE nome = %s"
# val = ("Gael", )
# cursor.execute(sql, val)
# db.commit()

# print(cursor.rowcount, "record(s) deleted")


# ------------------------ Apagar Tabelas ------------------------
# sql = "DROP TABLE pessoa"
# cursor.execute(sql)


# ---------------------- Apagar Tabelas e apenas Existir ----------------------
# sql = "DROP TABLE IF EXISTS pessoa"
# cursor.execute(sql)

# ------------------------ ATualizar Tabela ------------------------
# sql = "UPDATE pessoa SET telefones = %s WHERE telefones = %s"
# val = ("12345678911", "88766546545")
# cursor.execute(sql, val)
# db.commit()

# print(cursor.rowcount, "record(s) affected")


# -------------------- LIMITES(primeiros dados) da tabela --------------------
# sql = "SELECT * FROM pessoa LIMIT 2"
# cursor.execute(sql)
# result = cursor.fetchall()
# for i in result:
#     print(i)


# -------------------- LIMITES(dados setados) da tabela --------------------
# sql = "SELECT * FROM pessoa LIMIT 1 OFFSET 2" #começa na posição 2

# cursor.execute(sql)
# result = cursor.fetchall()
# for i in result:
#     print(i)
