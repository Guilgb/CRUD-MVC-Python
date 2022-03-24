from src.modelo.Estado import Estado
from src.modelo.Cidade import Cidade
from src.modelo.Escolaridade import Escolaridade
from src.modelo.Telefones import Telefones
from src.modelo.Aluno import Aluno
from src.modelo.Conection import Conection


class DAOAluno:
    def __init__(self) -> None:
        pass

    def insertAluno(i: list):
        try:
            con = Conection.getConection('')

            cursor = con.cursor()

            nomePessoa = i[0]
            telefones = Telefones(i[1])
            estados = Estado(i[3])
            cidades = Cidade(i[2], estados)
            escolaridades = Escolaridade(i[4])
            novoAluno = Aluno(nomePessoa, telefones,
                              cidades, escolaridades)

            # SQL TELEFONE
            sqlTelefone = "INSERT INTO Telefones(numeroTelefone) value(%s)"
            valueTelefone = (novoAluno.telefones.numeroTelefone)
            cursor.execute(sqlTelefone, valueTelefone)

            def idTelefone():
                sqlIdtelefone = "SELECT idTelefone FROM Telefones where numeroTelefone=%s"
                valueIdTelefones = (novoAluno.telefones.numeroTelefone)
                cursor.execute(sqlIdtelefone, valueIdTelefones)
                resultTelefone = cursor.fetchone()
                for reTelefone in resultTelefone:
                    return reTelefone

            # SQL ESTADO
            sqlEstado = "INSERT INTO Estado(nomeEstado) value(%s)"
            valueEstado = (novoAluno.cidades.estado.estado)
            cursor.execute(sqlEstado, valueEstado)

            def idEstado():
                sqlIdEstado = "SELECT idEstado FROM Estado where nomeEstado=%s"
                valueIdEstado = (novoAluno.cidades.estado.estado)
                cursor.execute(sqlIdEstado, valueIdEstado)
                resultEstado = cursor.fetchone()
                for reEstado in resultEstado:
                    return reEstado

            # SQL CIDADE
            sqlCidade = "INSERT INTO Cidades(nomeCidade) value(%s)"
            valueCidade = (novoAluno.cidades.cidade)
            cursor.execute(sqlCidade, valueCidade)

            def idCidade():
                sqlIdCidade = "SELECT idCidade FROM Cidades where nomeCidade=%s"
                valueIdCidade = (novoAluno.cidades.cidade)
                cursor.execute(sqlIdCidade, valueIdCidade)
                resultCidade = cursor.fetchone()
                for reCidade in resultCidade:
                    return reCidade

            # SQL ESCOLARIDADE
            sqlEscolaridade = "INSERT INTO Escolaridade(nomeEscolaridade) value(%s)"
            valueEscolaridade = (novoAluno.escolaridades.escolaridade)
            cursor.execute(sqlEscolaridade, valueEscolaridade)

            def idEscolaridade():
                sqlIdEscolaridade = "SELECT idEscolaridade FROM Escolaridade where nomeEscolaridade=%s"
                valueIdEscolaridade = (novoAluno.escolaridades.escolaridade)
                cursor.execute(sqlIdEscolaridade, valueIdEscolaridade)
                resultEscolaridade = cursor.fetchone()

                for reEscolaridade in resultEscolaridade:
                    return reEscolaridade

            # SQL Aluno
            sqlAluno = "INSERT INTO Aluno(nomeAluno, idTelefone, idCidade, idEscolaridade) values(%s, %s, %s, %s)"
            valuesAluno = (novoAluno.nomePessoa, idTelefone(),
                           idCidade(), idEscolaridade())
            cursor.execute(sqlAluno, valuesAluno)
            con.commit()

        except TypeError as error:
            print("Failed ", error)

    def listarAlunos(self):
        try:
            lista = []
            con = Conection.getConection("Iniciando Conexão")
            cursor = con.cursor()
            sql = "select a.idAluno, a.nomeAluno, t.numeroTelefone, c.nomeCidade, es.nomeEscolaridade from Aluno a inner join Telefones t on(a.idTelefone = t.idTelefone) inner join Cidades c on (a.idCidade = c.idCidade) inner join Escolaridade es on(a.idEscolaridade = es.idEscolaridade)"
            cursor.execute(sql)
            records = cursor.fetchall()

            for i in records:
                lista.append(i)
            return lista
        except TypeError as error:
            print("Failed ", error)

    def deleteAluno(nomeAluno):
        try:
            con = Conection.getConection("Iniciando Conexão")
            cursor = con.cursor()
            sql = 'DELETE from Aluno where nomeAluno = %s'
            cursor.execute(sql, nomeAluno)
            con.commit()
        except TypeError as error:
            print("Failed ", error)

        finally:
            cursor.close()
            con.close()
            print('SQL Connection Close')

    def updateAluno(i: list):
        try:
            # CONNECTION
            con = Conection.getConection('')
            cursor = con.cursor()

            # SQL UPDATE NOME
            sqlAlunoUpdate = "UPDATE Aluno set nomeAluno=%s where idAluno=%s "
            valuesAlunoUpdate = (
                i[1], i[0])
            cursor.execute(sqlAlunoUpdate, valuesAlunoUpdate)

            # SQL UPDATE TELEFONE
            def idTelefone():
                sqlIdtelefone = "SELECT idTelefone FROM Aluno where idAluno=%s"
                valueIdTelefones = (i[0])
                cursor.execute(sqlIdtelefone, valueIdTelefones)
                resultTelefone = cursor.fetchone()
                for reTelefone in resultTelefone:
                    return reTelefone

            sqlUpdateTelefone = "UPDATE Telefones set numeroTelefone=%s where idTelefone=%s"
            valuesUpdateTelefone = (i[2], idTelefone())
            cursor.execute(sqlUpdateTelefone, valuesUpdateTelefone)

            # SQL UPDATE CIDADE

            def idCidade():
                sqlIdCidade = "SELECT idCidade FROM Aluno where idAluno=%s"
                valueIdCidade = (i[0])
                cursor.execute(sqlIdCidade, valueIdCidade)
                resultCidade = cursor.fetchone()
                for reCidade in resultCidade:
                    return reCidade

            sqlUpdateCidade = "UPDATE Cidades set nomeCidade=%s where idCidade=%s"
            valuesUpdateCidade = (i[3], idCidade())
            cursor.execute(sqlUpdateCidade, valuesUpdateCidade)

            # SQL ESCOLARIDADE
            def idEscolaridade():
                sqlIdEscolaridade = "SELECT idEscolaridade FROM Aluno where idAluno=%s"
                valueIdEscolaridade = (i[0])
                cursor.execute(sqlIdEscolaridade, valueIdEscolaridade)
                resultEscolaridade = cursor.fetchone()
                for reEscolaridade in resultEscolaridade:
                    return reEscolaridade

            sqlUpdateEscolaridade = "UPDATE Escolaridade set nomeEscolaridade=%s where idEscolaridade=%s"
            valuesUpdateEscolaridade = (i[4], idEscolaridade())
            cursor.execute(sqlUpdateEscolaridade, valuesUpdateEscolaridade)

            con.commit()

        except TypeError as error:
            print("Failed", error)


# lista = ['Guilherme Gonçalves', 'telefone', 'CE', 'cidade', 'escolaridade']
# inserir = DAOAluno.insertAluno(lista)
