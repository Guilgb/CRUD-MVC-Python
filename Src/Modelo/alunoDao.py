from estado import Estado
from cidade import Cidade
from escolaridade import Escolaridade
from telefones import Telefones
from aluno import Aluno
from conection import Conection


class DAOAluno:
    def __init__(self) -> None:
        pass

    def insertAluno(self):
        nomePessoa = input('\nSeu Nome:')
        telefone = input('\nSeu Telefone:')
        uf = input('\nSeu Estado:')
        cidade = input('\nSua Cidade:')
        escolaridade = input('\nSua Escolaridade:')

        cadastrandoAluno = input('Deseja Cadastrar o Aluno ? y/n')

        if(cadastrandoAluno == 'y'):
            telefones = Telefones(telefone)
            estado = Estado(uf)
            cidades = Cidade(cidade)
            escolaridades = Escolaridade(escolaridade)
            novoAluno = Aluno(nomePessoa, telefones,
                              cidades, escolaridades)

        con = Conection.getConection('Iniciando Conecxão')
        cursor = con.cursor()

        sqlTelefone = "insert into Telefones(numeroTelefone) value(%s)"
        valuesTelefone = (novoAluno.telefones)
        cursor.execute(sqlTelefone, valuesTelefone)

        sqlEstado = f"insert into Estado(nomeEstado) value('{estado.estado}')"
        cursor.execute(sqlEstado)

        sqlCidade = "insert into Cidades(nomeCidade) value(%s)"
        valuesCidade = (novoAluno.cidades)
        cursor.execute(sqlCidade, valuesCidade)

        sqlEscolaridade = "insert into Escolaridade(nomeEscolaridade) value(%s)"
        valuesEscolaridade = (novoAluno.escolaridades)
        cursor.execute(sqlEscolaridade, valuesEscolaridade)

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

        def idEscolaridade():
            cursor.execute(
                f"SELECT idEscolaridade FROM Escolaridade where nomeEscolaridade= '{escolaridade}'"
            )
            resultescolaridade = cursor.fetchone()
            for escolaridaderes in resultescolaridade:
                return escolaridaderes

        cursor.execute(
            f"INSERT INTO Aluno(nomeAluno, idTelefone, idCidade, idEscolaridade) values('{nomePessoa}', '{idTelefone()}', '{idCidade()}', '{idEscolaridade()}')"
        )

        con.commit()

    def listarAlunos(self):
        try:
            con = Conection.getConection("Iniciando Conexão")
            cursor = con.cursor()
            sql = "select a.nomeAluno, t.numeroTelefone, c.nomeCidade, es.nomeEscolaridade from Aluno a inner join Telefones t on(a.idTelefone = t.idTelefone) inner join Cidades c on (a.idCidade = c.idCidade) inner join Escolaridade es on (a.idEscolaridade = es.idEscolaridade);"
            cursor.execute(sql)
            records = cursor.fetchall()

            for row in records:
                print("Nome: =", row[0])
                print("Telefone: =", row[1])
                print("Cidade: =", row[2])
                print("Escolaridade: =", row[3])
        except TypeError as error:
            print("Failed ", error)

        finally:
            cursor.close()
            con.close()
            print('SQL Connection Close')

    def deleteAluno(self):
        try:
            con = Conection.getConection("Iniciando Conexão")
            cursor = con.cursor()
            nomeAluno = input('Nome Aluno: ')
            sql = 'DELETE from Aluno where nomeAluno = %s'
            cursor.execute(sql, nomeAluno)
            con.commit()
        except TypeError as error:
            print("Failed ", error)

        finally:
            cursor.close()
            con.close()
            print('SQL Connection Close')
