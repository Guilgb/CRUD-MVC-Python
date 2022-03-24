from src.modelo.Estado import Estado
from src.modelo.Cidade import Cidade
from src.modelo.Telefones import Telefones
from src.modelo.Instrutor import Instrutor
from src.controller.conection import Conection


class DAOInstrutor:
    def __init__(self) -> None:
        pass

    def inserirInstrutor(i: list):
        try:
            con = Conection.getConection('')

            cursor = con.cursor()
            telefones = Telefones(i[1])
            estados = Estado(i[3])
            cidades = Cidade(i[2], estados)
            novoInstrutor = Instrutor(
                i[0], telefones, cidades, i[4])

            # SQL TELEFONE
            sqlTelefone = "INSERT INTO Telefones(numeroTelefone) value(%s)"
            valueTelefone = (novoInstrutor.telefones.numeroTelefone)
            cursor.execute(sqlTelefone, valueTelefone)

            def idTelefone():
                sqlIdtelefone = "SELECT idTelefone FROM Telefones where numeroTelefone=%s"
                valueIdTelefones = (novoInstrutor.telefones.numeroTelefone)
                cursor.execute(sqlIdtelefone, valueIdTelefones)
                resultTelefone = cursor.fetchone()
                for reTelefone in resultTelefone:
                    return reTelefone

            # SQL ESTADO
            sqlEstado = "INSERT INTO Estado(nomeEstado) value(%s)"
            valueEstado = (novoInstrutor.cidades.estado.estado)
            cursor.execute(sqlEstado, valueEstado)

            def idEstado():
                sqlIdEstado = "SELECT idEstado FROM Estado where nomeEstado=%s"
                valueIdEstado = (novoInstrutor.cidades.estado.estado)
                cursor.execute(sqlIdEstado, valueIdEstado)
                resultEstado = cursor.fetchone()
                for reEstado in resultEstado:
                    return reEstado

            # SQL CIDADE
            sqlCidade = "INSERT INTO Cidades(nomeCidade) value(%s)"
            valueCidade = (novoInstrutor.cidades.cidade)
            cursor.execute(sqlCidade, valueCidade)

            def idCidade():
                sqlIdCidade = "SELECT idCidade FROM Cidades where nomeCidade=%s"
                valueIdCidade = (novoInstrutor.cidades.cidade)
                cursor.execute(sqlIdCidade, valueIdCidade)
                resultCidade = cursor.fetchone()
                for reCidade in resultCidade:
                    return reCidade

            # SQL INSTRUTOR
            sqlInstrutor = "INSERT INTO Instrutor(nomeInstrutor, formacao, idTelefone, idCidade) values(%s, %s, %s, %s)"
            valuesInstrutor = (novoInstrutor.nomePessoa, novoInstrutor.formacao,
                               idTelefone(), idCidade()
                               )
            cursor.execute(sqlInstrutor, valuesInstrutor)

            con.commit()

        except TypeError as error:
            print("Failed", error)

        finally:
            cursor.close()
            con.close()
            print('CONNECTION CLOSE')

    def deleteInstrutor(nomeInstrutor):
        try:
            con = Conection.getConection('')
            cursor = con.cursor()
            sql = "DELETE from Instrutor where nomeInstrutor = %s"
            value = (nomeInstrutor)
            cursor.execute(sql, value)
        except TypeError as error:
            print("Failed", error)

        finally:
            cursor.close()
            con.close()

    def updateInstrutor(i: list):
        try:
            # CONNECTION
            con = Conection.getConection('')
            cursor = con.cursor()

            # SQL UPDATE NOME
            sqlInstrutorUpdate = "UPDATE Instrutor set nomeInstrutor=%s, formacao=%s where idInstrutor=%s "
            valuesInstrutorUpdate = (
                i[1], i[4], i[0])
            cursor.execute(sqlInstrutorUpdate, valuesInstrutorUpdate)

            # SQL UPDATE TELEFONE
            def idTelefone():
                sqlIdtelefone = "SELECT idTelefone FROM Instrutor where idInstrutor=%s"
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
                sqlIdCidade = "SELECT idCidade FROM Instrutor where idInstrutor=%s"
                valueIdCidade = (i[0])
                cursor.execute(sqlIdCidade, valueIdCidade)
                resultCidade = cursor.fetchone()
                for reCidade in resultCidade:
                    return reCidade

            sqlUpdateCidade = "UPDATE Cidades set nomeCidade=%s where idCidade=%s"
            valuesUpdateCidade = (i[3], idCidade())
            cursor.execute(sqlUpdateCidade, valuesUpdateCidade)

            con.commit()

        except TypeError as error:
            print("Failed", error)

        finally:
            cursor.close()
            con.close()

    def listarInstrutor(self):
        try:
            lista = []
            con = Conection.getConection("Iniciando Conexão")
            cursor = con.cursor()
            sql = "select i.idInstrutor, i.nomeInstrutor, t.numeroTelefone, c.nomeCidade, i.formacao from Instrutor i inner join Telefones t on(i.idTelefone = t.idTelefone) inner join Cidades c on(i.idCidade = c.idCidade)"
            cursor.execute(sql)
            records = cursor.fetchall()

            for i in records:
                lista.append(i)
            return lista
        except TypeError as error:
            print("Failed ", error)


# lista = ['NOME', 'TELEFONE', 'CIDADE', 'ESTADO', 'FORMCAO']
# init = DAOInstrutor.inserirInstrutor(lista)
