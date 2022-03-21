from curso import Curso
from filial import Filial
from area import Area
from conection import Conection
from turma import Turma


class DAOTurma:
    def __init__(self) -> None:
        pass

    def inserirTurma(self):
        try:
            nomeTurma = input('Digite o nome da turma:')
            horaInicio = input('Hora incio: ')
            horaFim = input('Hora fim: ')
            diaInicio = input('Dia inicio: ')
            diaFim = input('Dia fim: ')
            nomeCurso = input('Digite a area do curso: ')
            chCurso = input('Digite o CH do curso: ')
            nomeArea = input('Digit o nome da Area: ')
            nomeFilial = input('Digite a sua filial: ')
            localidade = input('Digite a localidade: ')
            nomeInstrutor = input(
                'Digite o nome do instrutor a ser cadastrado: ')

            cadastrarTurma = input('Deseja cadastrar turma ? y/n ')

            if(cadastrarTurma == 'y'):
                area = Area(nomeArea)
                curso = Curso(nomeCurso, chCurso, area)
                filial = Filial(nomeFilial, localidade)
                novaTurma = Turma(nomeTurma, horaInicio, horaFim,
                                  diaInicio, diaFim, curso,
                                  filial, nomeInstrutor)

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

    def deleteTurma(self):
        try:
            nomeTurma = input(
                "Digite o nome da turma a ser deletado: ")

            con = Conection.getConection('')
            cursor = con.cursor()
            sql = "DELETE from Turma where nomeTurma = %s"
            cursor.execute(sql, nomeTurma)
        except TypeError as error:
            print("Failed", error)

        finally:
            cursor.close()
            con.close()

    def updateTurma(self):
        nomeTurma = input('Digite o nome da turma que você deseja atualizar: ')
        novonometurma = input('Digite o novo nome da turma: ')
        novahorai = input('Nova Hora inicial: ')
        novahoraf = input('Nova Hora final: ')
        novodiai = input('Novo dia inicial: ')
        novodiaf = input('Novo dia final: ')
        novaFilial = input('Nova filial')
        novalocalidadefilial = input('Nova localidade da filial: ')
        novoinstrutor = input('Novo instrutor')
        novocurso = input('Novo Curso')

        con = Conection.getConection('')
        cursor = con.cursor()

        def idFilial():
            sqlIdFilial = "SELECT idFilial FROM Turma where nomeTurma=%s"
            valueIdFilial = (nomeTurma)
            cursor.execute(sqlIdFilial, valueIdFilial)

            resultFilial = cursor.fetchone()
            for reFilial in resultFilial:
                return reFilial

        def idInstrutor():
            sqlIdInstrutor = "SELECT idInstrutor FROM Turma where nomeTurma=%s"
            valueIdInstrutor = (nomeTurma)
            cursor.execute(sqlIdInstrutor, valueIdInstrutor)

            resultIdInstrutor = cursor.fetchone()
            for reInstrutor in resultIdInstrutor:
                return reInstrutor

        def idInstrutorNovo():
            newins = "SELECT idInstrutor FROM Instrutor where nomeInstrutor=%s"
            valuenewins = (novoinstrutor)
            cursor.execute(newins, valuenewins)
            resultnIdInstrutor = cursor.fetchone()
            for renInstrutor in resultnIdInstrutor:
                return renInstrutor

        def idCurso():
            sqlIdCurso = "SELECT idCurso FROM Turma where nomeTurma=%s"
            valueIdCurso = (nomeTurma)
            cursor.execute(sqlIdCurso, valueIdCurso)
            resultIdCurso = cursor.fetchone()
            for reCurso in resultIdCurso:
                return reCurso

        # SQL UPDATE FILIAL

        sqlUpdateFilial = "UPDATE Filial set nomeFilial=%s, localidadeFilial=%s where idFilial=%s "
        valuesUpdateFilial = (novaFilial, novalocalidadefilial, idFilial())
        cursor.execute(sqlUpdateFilial, valuesUpdateFilial)

        # SQL UPDATE INSTRUTOR

        sqlUpdateInstrutor = "UPDATE Turma set idInstrutor=%s where idInstrutor=%s"
        valueUpdateinstrutor = (idInstrutor(), idInstrutorNovo())
        cursor.execute(sqlUpdateInstrutor, valueUpdateinstrutor)

        # SQL UPDATE CURSO
        sqlUpdateCurso = "UPDATE Curso set nomeCurso=%s where idCurso=%s"
        valueUpdateCurso = (novocurso, idCurso())
        cursor.execute(sqlUpdateCurso, valueUpdateCurso)

        # SQL UPDATE TURMA
        sqlUpdateTurma = "UPDATE Turma set nomeTurma=%s, horaInicio=%s, horaFim=%s, diaInicio=%s, diaFim=%s"
        valuesUpdateTurma = (novonometurma, novahorai,
                             novahoraf, novodiai, novodiaf)
        cursor.execute(sqlUpdateTurma, valuesUpdateTurma)
        con.commit()


update = DAOTurma.updateTurma('')
