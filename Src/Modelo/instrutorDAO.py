from cidade import Cidade
from estado import Estado
from telefones import Telefones
from instrutor import Instrutor
from conection import Conection


class DAOInstrutor:
    def __init__(self) -> None:
        pass

    def inserirInstrutor(self):
        nomeInstrutor = input('Seu nome: ')
        formacao = input('Sua Formação: ')
        telefone = input('Seu Telefone: ')
        uf = input('Seu Estado: ')
        cidade = input('Sua Cidae: ')

        cadastroInstrutor = input('Deseja cadastrar o Instrutor? y/n ')

        if(cadastroInstrutor == 'y'):
            telefones = Telefones(telefone)
            estado = Estado(uf)
            cidades = Cidade(cidade)
            novoInstrutor = Instrutor(
                nomeInstrutor, telefones, cidades, formacao)

        con = Conection.getConection('Iniciando Conexão')

        cursor = con.cursor()

        sqlTelefone = "insert into Telefones(numeroTelefone) value(%s)"
        valuesTelefone = (novoInstrutor.telefones)
        cursor.execute(sqlTelefone, valuesTelefone)

        sqlEstado = f"insert into Estado(nomeEstado) value('{estado.estado}')"
        cursor.execute(sqlEstado)

        sqlCidade = "insert into Cidades(nomeCidade) value(%s)"
        valuesCidade = (novoInstrutor.cidades)
        cursor.execute(sqlCidade, valuesCidade)

        con.commit()

        def idCidade():
            cursor.execute(f"select idCidade from Cidades where nomeCidade='{cidade}'"
                           )
            resultcidade = cursor.fetchone()
            for cidaderes in resultcidade:
                return cidaderes

        def idTelefone():
            cursor.execute(f"select idTelefone from Telefones where numeroTelefone='{telefone}'"
                           )
            resulttelefone = cursor.fetchone()
            for telefoneres in resulttelefone:
                return telefoneres

        cursor.execute(
            f"INSERT INTO Instrutor(nomeInstrutor, formacao, idTelefone, idCidade) values('{nomeInstrutor}', '{formacao}', '{idTelefone()}', '{idCidade()}')"
        )

        con.commit()
