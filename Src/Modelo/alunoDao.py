from turtle import update
from estado import Estado
from cidade import Cidade
from escolaridade import Escolaridade
from telefones import Telefones
from aluno import Aluno
from conection import Conection


class DAOAluno:
    def __init__(self) -> None:
        pass

    def insertAluno(i: list):
        try:
            # nomePessoa = input('\nSeu Nome:')
            # telefone = input('\nSeu Telefone:')
            # uf = input('\nSeu Estado:')
            # cidade = input('\nSua Cidade:')
            # escolaridade = input('\nSua Escolaridade:')

            con = Conection.getConection('')

            cursor = con.cursor()

            nomePessoa = i[0]
            telefones = Telefones(i[1])
            estados = Estado(i[2])
            cidades = Cidade(i[3], estados)
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

    def updateAluno(self):
        try:
            nomeAluno = input("Aluno a ser atualizado: ")

            novoNomeAluno = input("Digite o novo nome: ")
            novoNumeroTelefone = input(
                'Digite o seu novo numero de telefone: ')
            novaCidade = input('Digite o nome da sua nova cidade: ')
            novaEscolaridade = input('Digite sua nova Escolaridade: ')

            # CONNECTION
            con = Conection.getConection('')
            cursor = con.cursor()

            # SQL UPDATE NOME
            sqlAlunoUpdate = "UPDATE Aluno set nomeAluno=%s where nomeAluno=%s "
            valuesAlunoUpdate = (
                novoNomeAluno, nomeAluno)
            cursor.execute(sqlAlunoUpdate, valuesAlunoUpdate)

            # SQL UPDATE TELEFONE
            def idTelefone():
                sqlIdtelefone = "SELECT idTelefone FROM Aluno where nomeAluno=%s"
                valueIdTelefones = (novoNomeAluno)
                cursor.execute(sqlIdtelefone, valueIdTelefones)
                resultTelefone = cursor.fetchone()
                for reTelefone in resultTelefone:
                    return reTelefone

            sqlUpdateTelefone = "UPDATE Telefones set numeroTelefone=%s where idTelefone=%s"
            valuesUpdateTelefone = (novoNumeroTelefone, idTelefone())
            cursor.execute(sqlUpdateTelefone, valuesUpdateTelefone)

            # SQL UPDATE CIDADE

            def idCidade():
                sqlIdCidade = "SELECT idCidade FROM Aluno where nomeAluno=%s"
                valueIdCidade = (novoNomeAluno)
                cursor.execute(sqlIdCidade, valueIdCidade)
                resultCidade = cursor.fetchone()
                for reCidade in resultCidade:
                    return reCidade

            sqlUpdateCidade = "UPDATE Cidades set nomeCidade=%s where idCidade=%s"
            valuesUpdateCidade = (novaCidade, idCidade())
            cursor.execute(sqlUpdateCidade, valuesUpdateCidade)

            # SQL ESCOLARIDADE
            def idEscolaridade():
                sqlIdEscolaridade = "SELECT idEscolaridade FROM Aluno where nomeAluno=%s"
                valueIdEscolaridade = (novoNomeAluno)
                cursor.execute(sqlIdEscolaridade, valueIdEscolaridade)
                resultEscolaridade = cursor.fetchone()
                for reEscolaridade in resultEscolaridade:
                    return reEscolaridade

                    sqlUpdateCidade = "UPDATE Cidades set nomeCidade=%s where idCidade=%s"

            sqlUpdateEscolaridade = "UPDATE Escolaridade set nomeEscolaridade=%s where idEscolaridade=%s"
            valuesUpdateEscolaridade = (novaEscolaridade, idEscolaridade())
            cursor.execute(sqlUpdateEscolaridade, valuesUpdateEscolaridade)

            con.commit()

        except TypeError as error:
            print("Failed", error)

        finally:
            cursor.close()
            con.close()
