from matricula import Matricula
from conection import Conection


class DAOMatricula:
    def __init__(self) -> None:
        pass

    def inserirMatricula(self):
        try:
            nomeTurma = input(
                "Digite o nome da turma na qual deseja cadastrar: ")
            aluno = input('Digite o nome do aluno a cadastrar: ')

            cadastroMatricula = input(
                'Deseja realmente cadastrar sua matricula (y/n): ')
            if(cadastroMatricula == 'y'):
                novaMatricula = Matricula(aluno, nomeTurma)

            # CONEXÃO COM O BANCO
            con = Conection.getConection("")
            cursor = con.cursor()

            # SQL BUSCA ALUNO
            def idAluno():
                sqlAluno = "SELECT idAluno FROM Aluno where nomeAluno=%s"
                valueAluno = (novaMatricula.aluno)
                cursor.execute(sqlAluno, valueAluno)

                resultAluno = cursor.fetchone()
                for reAluno in resultAluno:
                    return reAluno

            # SQL BUSCA TURMA
            def idTurma():
                sqlTurma = "SELECT idTurma FROM Turma where nomeTurma=%s"
                valueTurma = (novaMatricula.turma)
                cursor.execute(sqlTurma, valueTurma)

                resultTurma = cursor.fetchone()
                for reTurma in resultTurma:
                    return reTurma

            # CRIA MATRICULA
            sqlMatricula = "INSERT INTO Matricula(idAluno, idTurma) values(%s, %s)"
            valueMatricula = (idAluno(), idTurma())
            cursor.execute(sqlMatricula, valueMatricula)

        except TypeError as error:
            print("Failed", error)

        finally:
            cursor.close()
            con.close()
            print('CONNECTION CLOSE')

    def deletMatricula(self):
        try:
            idMatricula = input(
                "Digite o IDe da matricula a ser deletada: ")

            con = Conection.getConection('')
            cursor = con.cursor()
            sql = "DELETE from Matricula where idMatricula = %s"
            cursor.execute(sql, idMatricula)
        except TypeError as error:
            print("Failed", error)

        finally:
            cursor.close()
            con.close()

    def updateMatricula(self):
        try:
            nomeMatricula = input(
                "Digite o nome da Matricula a ser atualizado: ")

            nomeMatriculaUpdate = input("Digite o novo nome: ")
            formacao = input("Digite a sua nova formçao: ")
            con = Conection.getConection('')
            cursor = con.cursor()

            sqlInstrutorUpdate = "UPDATE Matricula set idAluno=%s, idTurma=%s where idMatricula=%s "
            valuesInstrutorUpdate = (
                nomeMatriculaUpdate, formacao, nomeMatricula)
            cursor.execute(sqlInstrutorUpdate, valuesInstrutorUpdate)
            con.commit()

        except TypeError as error:
            print("Failed", error)

        finally:
            cursor.close()
            con.close()
