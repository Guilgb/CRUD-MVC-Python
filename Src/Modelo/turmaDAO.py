from curso import Curso
from filial import Filial
from area import Area
from conection import Conection
from turma import Turma


class DAOTurma:
    def __init__(self) -> None:
        pass

    def inserirTurma(i: list):
        try:
            area = Area(i[5])
            curso = Curso(i[6], i[7], area)
            filial = Filial(i[8], i[9])
            novaTurma = Turma(i[0], i[1], i[2],
                              i[3], i[4], curso,
                              filial, i[10])

            con = Conection.getConection("Inciando conexão")
            cursor = con.cursor()

            # SQL AREA
            sqlArea = "INSERT INTO Area(nomeArea) value(%s)"
            valueArea = (novaTurma.curso.areas.area)
            cursor.execute(sqlArea, valueArea)

            def idArea():
                sqlIdArea = "SELECT idArea FROM Area where nomeArea=%s"
                valueIdArea = (novaTurma.curso.areas.area)
                cursor.execute(sqlIdArea, valueIdArea)
                resultArea = cursor.fetone()
                for reArea in resultArea:
                    return reArea

            # SQL CURSO
            sqlCurso = "INSERT INTO Curso(nomeCurso, chCurso) value(%s, %s)"
            valueCurso = (novaTurma.curso.curso, novaTurma.curso.chCurso)
            cursor.execute(sqlCurso, valueCurso)

            def idCurso():
                sqlIdCurso = "SELECT idCurso FROM Curso where nomeCurso=%s"
                valueIdCurso = (novaTurma.curso.curso)
                cursor.execute(sqlIdCurso, valueIdCurso)
                resultIdCurso = cursor.fetchone()
                for reCurso in resultIdCurso:
                    return reCurso

            # SQL FILIAL
            sqlFilial = "INSERT INTO Filial(nomeFilial, localidadeFilial) value(%s, %s)"
            valueFilial = (novaTurma.filial.nomeFilial,
                           novaTurma.filial.localidade)
            cursor.execute(sqlFilial, valueFilial)

            def idFilial():
                sqlIdFilial = "SELECT idFilial FROM Filial where nomeFilial=%s"
                valueIdFilial = (novaTurma.filial.nomeFilial)
                cursor.execute(sqlIdFilial, valueIdFilial)

                resultFilial = cursor.fetchone()
                for reFilial in resultFilial:
                    return reFilial

            def instrutor():
                sqlIdInstrutor = "SELECT idInstrutor FROM Instrutor where nomeInstrutor=%s"
                valueIdInstrutor = (novaTurma.idInstrutor)
                cursor.execute(sqlIdInstrutor, valueIdInstrutor)

                resultIdInstrutor = cursor.fetchone()
                for reInstrutor in resultIdInstrutor:
                    return reInstrutor

            # SQL Turma

            sqlTurma = "INSERT INTO TURMA(nomeTurma, horaInicio, horaFim, diaInicio, diaFim, idCurso, idFilial, idInstrutor) values(%s, %s, %s, %s, %s, %s, %s, %s)"
            valueTurma = (novaTurma.nomeTurma, novaTurma.horaInicio, novaTurma.horaFim, novaTurma.diaInicio,
                          novaTurma.diaFim, idCurso(), idFilial(), instrutor())
            cursor.execute(sqlTurma, valueTurma)

            con.commit()

        except TypeError as error:
            print("Failed", error)

        finally:
            cursor.close()
            con.close()
            print('CONNECTION CLOSE')

    def deleteTurma(nomeTurma):
        try:
            con = Conection.getConection('')
            cursor = con.cursor()
            sql = "DELETE from Turma where nomeTurma = %s"
            value = (nomeTurma)
            cursor.execute(sql, value)
        except TypeError as error:
            print("Failed", error)

        finally:
            cursor.close()
            con.close()

    def updateTurma(i: list):
        con = Conection.getConection('')
        cursor = con.cursor()

        def idFilial():
            sqlIdFilial = "SELECT idFilial FROM Turma where idTurma=%s"
            valueIdFilial = (i[0])
            cursor.execute(sqlIdFilial, valueIdFilial)

            resultFilial = cursor.fetchone()
            for reFilial in resultFilial:
                return reFilial

        def idInstrutor():
            sqlIdInstrutor = "SELECT idInstrutor FROM Turma where idTurma=%s"
            valueIdInstrutor = (i[0])
            cursor.execute(sqlIdInstrutor, valueIdInstrutor)

            resultIdInstrutor = cursor.fetchone()
            for reInstrutor in resultIdInstrutor:
                return reInstrutor

        def idInstrutorNovo():
            newins = "SELECT idInstrutor FROM Instrutor where nomeInstrutor=%s"
            valuenewins = (i[10])
            cursor.execute(newins, valuenewins)
            resultnIdInstrutor = cursor.fetchone()
            for renInstrutor in resultnIdInstrutor:
                return renInstrutor

        def idCurso():
            sqlIdCurso = "SELECT idCurso FROM Turma where idTurma=%s"
            valueIdCurso = (i[0])
            cursor.execute(sqlIdCurso, valueIdCurso)
            resultIdCurso = cursor.fetchone()
            for reCurso in resultIdCurso:
                return reCurso

        # SQL UPDATE FILIAL

        sqlUpdateFilial = "UPDATE Filial set nomeFilial=%s, localidadeFilial=%s where idFilial=%s "
        valuesUpdateFilial = (i[8], i[9], idFilial())
        cursor.execute(sqlUpdateFilial, valuesUpdateFilial)

        # SQL UPDATE INSTRUTOR

        sqlUpdateInstrutor = "UPDATE Turma set idInstrutor=%s where idInstrutor=%s"
        valueUpdateinstrutor = (idInstrutor(), idInstrutorNovo())
        cursor.execute(sqlUpdateInstrutor, valueUpdateinstrutor)

        # SQL UPDATE CURSO
        sqlUpdateCurso = "UPDATE Curso set nomeCurso=%s, chCurso=%s where idCurso=%s"
        valueUpdateCurso = (i[6], i[7], idCurso())
        cursor.execute(sqlUpdateCurso, valueUpdateCurso)

        # SQL NOME TURMA

        # SQL UPDATE TURMA
        sqlUpdateTurma = "UPDATE Turma set nomeTurma=%s, horaInicio=%s, horaFim=%s, diaInicio=%s, diaFim=%s where idTurma=%s"
        valuesUpdateTurma = (i[1], i[2],
                             i[3], i[4], i[5], i[0])
        cursor.execute(sqlUpdateTurma, valuesUpdateTurma)
        con.commit()

    def listarTurma(self):
        try:
            lista = []
            con = Conection.getConection("Iniciando Conexão")
            cursor = con.cursor()
            sql = "select t.idTurma, t.nomeTurma, t.horaInicio, t.horaFim, t.diaInicio, t.diaFim, c.nomeCurso, c.chCurso, f.nomeFilial, f.localidadeFilial, i.nomeInstrutor from Turma t inner join Curso c on(t.idCurso = c.idCurso) inner join Filial f on(t.idFilial = f.idFilial) inner join Instrutor i on(t.idInstrutor = i.idInstrutor);"
            cursor.execute(sql)
            records = cursor.fetchall()

            for i in records:
                lista.append(i)
            return lista
        except TypeError as error:
            print("Failed ", error)
