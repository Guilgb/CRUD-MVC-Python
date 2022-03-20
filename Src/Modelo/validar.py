from pessoa import Pessoa
from aluno import Aluno
from telefones import Telefones
from estado import Estado
from cidade import Cidade
from escolaridade import Escolaridade
from area import Area
from curso import Curso
from filial import Filial
from turma import Turma
from conection import Conection


def inserir():
    nomePessoa = input('\nSeu Nome:')
    telefone = input('\nSeu Telefone:')
    uf = input('\nSeu Estado:')
    cidade = input('\nSua Cidade:')
    escolaridade = input('\nSua Escolaridade:')

    con = Conection.getConection('')

    cursor = con.cursor()

    telefones = Telefones(telefone)
    estados = Estado(uf)
    cidades = Cidade(cidade, estados)
    escolaridades = Escolaridade(escolaridade)
    novoAluno = Aluno(nomePessoa, telefones, cidades, escolaridades)

    print(novoAluno.nomePessoa, novoAluno.telefones.numeroTelefone,
          novoAluno.cidades.cidade, novoAluno.cidades.estado.estado,
          novoAluno.escolaridades.escolaridade)

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


inserir()
