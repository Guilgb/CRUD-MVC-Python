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
                sqlIdAluno = "SELECT idAluno FROM Aluno where nomeAluno=%s"
                valueIdAluno = (novaMatricula.aluno)
                cursor.execute(sqlIdAluno, valueIdAluno)

                resultIdAluno = cursor.fetchone()
                for reAluno in resultIdAluno:
                    return reAluno

            # SQL BUSCA TURMA
            def idTurma():
                sqlIdTurma = "SELECT idTurma FROM Turma where nomeTurma=%s"
                valueIdTurma = (novaMatricula.turma)
                cursor.execute(sqlIdTurma, valueIdTurma)

                resultIdTurma = cursor.fetchone()
                for reTurma in resultIdTurma:
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
            idMatricula = input("Digite sua Matricula: ")

            novaTurma = input('Digite a nova Tuma a ser atualizada')
            novoAluno = input("Digite o nome do Aluno que deseja atualizar: ")

            con = Conection.getConection("")
            cursor = con.cursor()

            # SQL BUSCA ALUNO
            def idAluno():
                sqlIdAluno = "SELECT idAluno FROM Aluno where nomeAluno=%s"
                valueIdAluno = (novoAluno)
                cursor.execute(sqlIdAluno, valueIdAluno)

                resultIdAluno = cursor.fetchone()
                for reAluno in resultIdAluno:
                    return reAluno

            # SQL BUSCA TURMA
            def idTurma():
                sqlIdTurma = "SELECT idTurma FROM Turma where nomeTurma=%s"
                valueIdTurma = (novaTurma)
                cursor.execute(sqlIdTurma, valueIdTurma)

                resultIdTurma = cursor.fetchone()
                for reTurma in resultIdTurma:
                    return reTurma

            sqlUpdateMatricula = "UPDATE Matricula set idTurma=%s, idAluno=%s where idMatricula=%s"
            valuesUpdateMatricula = (idTurma(), idAluno(), idMatricula)
            cursor.execute(sqlUpdateMatricula, valuesUpdateMatricula)

            con.commit()

        except TypeError as error:
            print("Failed", error)

        finally:
            cursor.close()
            con.close()
