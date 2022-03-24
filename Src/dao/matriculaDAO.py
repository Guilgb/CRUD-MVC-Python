from src.modelo.Matricula import Matricula
from src.controller.conection import Conection


class DAOMatricula:
    def __init__(self) -> None:
        pass

    def inserirMatricula(i: list):
        try:

            novaMatricula = Matricula(i[0], i[1])

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

    def deletMatricula(nomeAluno):
        try:
            con = Conection.getConection('')
            cursor = con.cursor()

            def idAluno():
                sqlIdAluno = "SELECT idAluno FROM Aluno where nomeAluno=%s"
                valueIdAluno = (nomeAluno)
                cursor.execute(sqlIdAluno, valueIdAluno)

                resultIdAluno = cursor.fetchone()
                for reAluno in resultIdAluno:
                    return reAluno

            sql = "DELETE from Matricula where idAluno = %s"
            cursor.execute(sql, idAluno())
        except TypeError as error:
            print("Failed", error)

        finally:
            cursor.close()
            con.close()

    def updateMatricula(i: list):
        try:
            con = Conection.getConection("")
            cursor = con.cursor()

            # SQL BUSCA ALUNO
            def idAluno():
                sqlIdAluno = "SELECT idAluno FROM Aluno where nomeAluno=%s"
                valueIdAluno = (i[1])
                cursor.execute(sqlIdAluno, valueIdAluno)

                resultIdAluno = cursor.fetchone()
                for reAluno in resultIdAluno:
                    return reAluno

            # SQL BUSCA TURMA
            def idTurma():
                sqlIdTurma = "SELECT idTurma FROM Turma where nomeTurma=%s"
                valueIdTurma = (i[2])
                cursor.execute(sqlIdTurma, valueIdTurma)

                resultIdTurma = cursor.fetchone()
                for reTurma in resultIdTurma:
                    return reTurma

            sqlUpdateMatricula = "UPDATE Matricula set idTurma=%s, idAluno=%s where idMatricula=%s"
            valuesUpdateMatricula = (idTurma(), idAluno(), i[0])
            cursor.execute(sqlUpdateMatricula, valuesUpdateMatricula)

            con.commit()

        except TypeError as error:
            print("Failed", error)

        finally:
            cursor.close()
            con.close()

    def listarMatricula(self):
        try:
            lista = []
            con = Conection.getConection("Iniciando Conexão")
            cursor = con.cursor()
            sql = "select m.idMatricula, a.nomeAluno, t.nomeTurma from Matricula m inner join Aluno a on(m.idAluno = a.idAluno) inner join Turma t on (m.idTurma = t.idTurma);"
            cursor.execute(sql)
            records = cursor.fetchall()

            for i in records:
                lista.append(i)
            return lista
        except TypeError as error:
            print("Failed ", error)
