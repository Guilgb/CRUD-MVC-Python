from cidade import Cidade
from estado import Estado
from telefones import Telefones
from instrutor import Instrutor
from conection import Conection


class DAOInstrutor:
    def __init__(self) -> None:
        pass

    def inserirInstrutor(self):
        nomePessoa = input('\nSeu Nome:')
        formacao = input("\nDigite sua formação: ")
        telefone = input('\nSeu Telefone:')
        uf = input('\nSeu Estado:')
        cidade = input('\nSua Cidade:')

        con = Conection.getConection('')

        cursor = con.cursor()
        cadastrarInstrutor = input("Deseja cadrastrar um Aluno (y/n): ")
        if(cadastrarInstrutor == 'y'):
            telefones = Telefones(telefone)
            estados = Estado(uf)
            cidades = Cidade(cidade, estados)
            novoInstrutor = Instrutor(
                nomePessoa, telefones, cidades, formacao)

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

    def deleteInstrutor(self):
        try:
            nomeInstrutor = input(
                "Digite o nome do instrutor a ser deletado: ")

            con = Conection.getConection('')
            cursor = con.cursor()
            sql = "DELETE from Instrutor where nomeInstrutor = %s"
            cursor.execute(sql, nomeInstrutor)
        except TypeError as error:
            print("Failed", error)

        finally:
            cursor.close()
            con.close()
