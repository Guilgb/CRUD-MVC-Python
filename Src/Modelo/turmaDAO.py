from curso import Curso
from filial import Filial
from area import Area
from conection import Conection
from turma import Turma


class DAOTurma:
    def __init__(self) -> None:
        pass

    def inserirTurma():
        horaInicio = input('Hora incio: ')
        horaFim = input('Hora fim: ')
        diaInicio = input('Dia inicio: ')
        diaFim = input('Dia fim: ')
        nomecurso = input('Digite a area do curso: ')
        chCurso = input('Digite o CH do curso: ')
        nomeArea = input('Digit o nome da Area: ')
        nomefilial = input('Digite a sua filial: ')
        localidade = input('Digite a localidade: ')

        cadastrarTurma = input('Deseja cadastrar a Turma ? y/n: ')
        if(cadastrarTurma == 'y'):
            area = Area(nomeArea)
            curso = Curso(nomecurso, chCurso, area)
            filial = Filial(nomefilial, localidade)
            novaTurma = Turma(horaInicio, horaFim, diaInicio,
                              diaFim, curso, filial)

        con = Conection.getConection('Iniciando Conexão')
        cursor = con.cursor()

        cursor.execute(
            f"insert into Area(nomeArea) value('{novaTurma.curso.areas}')")

        def idArea():
            cursor.execute(
                f"select idArea from Area where nomeArea='{novaTurma.curso.areas.area}'"
            )
            resultarea = cursor.fetchone()
            for area in resultarea:
                return area

        cursor.execute(
            f"insert into Curso(nomeCurso, chCurso, idArea) values('{novaTurma.curso.curso}', '{novaTurma.curso.chCurso}', {idArea()})")

        def idCurso():
            cursor.execute(
                f"select idCurso from Curso where nomeCurso='{novaTurma.curso.curso}'"
            )
            resultcurso = cursor.fetchone()
            for curso in resultcurso:
                return curso

        cursor.execute(
            f"insert into Filial(nomeFilial, localidadeFilial) values('{novaTurma.filial.nomeFilial}', '{novaTurma.filial.localidade}')")

        def idFilial():
            cursor.execute(
                f"select idFilial from Filial where='{novaTurma.filial.nomeFilial}'")
            resultfilial = cursor.fetchone()

            for filiais in resultfilial:
                return filiais

        cursor.execute(
            f"insert into Turma(horaInicio, horaFim, diaInicio, diaFim, idCurso, idFilial, idInstrutor) values('{horaInicio}', '{horaFim}', '{diaInicio}', '{diaFim}', '{idCurso()}', '{idFilial()}', '{idArea()}')")

        con.commit()


inseir = DAOTurma.inserirTurma()
