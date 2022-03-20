import pymysql
con = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='crud2'
)

cursor = con.cursor()
sql = ("select a.nomeAluno, t.numeroTelefone, c.nomeCidade, es.nomeEscolaridade from Aluno a inner join Telefones t on(a.idTelefone = t.idTelefone) inner join Cidades c on (a.idCidade = c.idCidade) inner join Escolaridade es on (a.idEscolaridade = es.idEscolaridade);")
# values = ('Guilherme', '88996431916', 'Cedro', 'Medio')
cursor.execute(sql)
con.commit()
