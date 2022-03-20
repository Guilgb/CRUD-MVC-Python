from curso import Curso
from filial import Filial
from area import Area
from conection import Conection
from turma import Turma


class DAOTurma:
    def __init__(self) -> None:
        pass

    def inserirTurma(self):
        horaInicio = input('Hora incio: ')
        horaFim = input('Hora fim: ')
        diaInicio = input('Dia inicio: ')
        diaFim = input('Dia fim: ')
        nomeCurso = input('Digite a area do curso: ')
        chCurso = input('Digite o CH do curso: ')
        nomeArea = input('Digit o nome da Area: ')
        nomeFilial = input('Digite a sua filial: ')
        localidade = input('Digite a localidade: ')
        nomeInstrutor = input('Digite o nome do instrutor a ser cadastrado: ')

        cadastrarTurma = input('Deseja cadastrar turma ? y/n ')

        if(cadastrarTurma == 'y'):
            area = Area(nomeArea)
            curso = Curso(nomeCurso, chCurso, area)
            filial = Filial(nomeFilial, localidade)
            novaTurma = Turma(horaInicio, horaFim,
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

        sqlTurma = "INSERT INTO TURMA(horaInicio, horaFim, diaInicio, diaFim, idCurso, idFilial, idInstrutor) values(%s, %s, %s, %s, %s, %s, %s)"
        valueTurma = (novaTurma.horaInicio, novaTurma.horaFim, novaTurma.diaInicio,
                      novaTurma.diaFim, idCurso(), idFilial(), instrutor())
        cursor.execute(sqlTurma, valueTurma)

        con.commit()
