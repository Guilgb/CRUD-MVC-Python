from curso import Curso
from filial import Filial
from area import Area
from conection import Conection


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
            curso = Curso(nomecurso, chCurso)
            filial = Filial(nomefilial, localidade)

        con = Conection.getConection('Iniciando Conexão')
        cursor = con.cursor()

        sqlArea = "insert into Area(nomeArea) value(%s)"
        valueArea = (nomeArea)
        cursor.execute(sqlArea, valueArea)

        def idArea():
            cursor.execute(
                f"select idArea from Area where nomeArea='{nomearea}'"
            )
            resultarea = cursor.fetchone()
            for area in resultarea:
                return area

        cursor.execute(
            f"insert into Curso(nomeCurso, chCurso, idArea) values('{nomecurso}', '{chCurso}', {idArea()})")

        def idCurso():
            cursor.execute(
                f"select idCurso from Curso where nomeCurso='{nomecurso}'"
            )
            resultcurso = cursor.fetchone()
            for curso in resultcurso:
                return curso

        cursor.execute(
            f"insert into Turma(horaInicio, horaFim, diaInicio, diaFim, idCurso, idFilial, idInstrutor) values('{horaInicio}', '{horaFim}', '{diaInicio}', '{diaFim}', '{idCurso()}', '{idFilial()}', '{idArea()}')")
