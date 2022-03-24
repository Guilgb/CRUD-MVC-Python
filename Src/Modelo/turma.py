from src.modelo.Curso import Curso
from src.modelo.Filial import Filial


class Turma():
    def __init__(self, nomeTurma: str, horaInicio: str, horaFim: str,
                 diaInicio: str, diaFim: str,
                 curso: Curso, filial: Filial, nomeInstrutor: str):
        self.__nomeTurma = nomeTurma
        self.__horaInicio = horaInicio
        self.__horaFim = horaFim
        self.__diaInicio = diaInicio
        self.__diaFim = diaFim
        self.__curso = curso
        self.__filial = filial
        self.__idInstrutor = nomeInstrutor

    @property
    def nomeTurma(self):
        return self.__nomeTurma

    @nomeTurma.setter
    def nomeTurma(self, nomeTurma):
        self.__nomeTurma = nomeTurma

    @property
    def horaInicio(self):
        return self.__horaInicio

    @horaInicio.setter
    def horaInicio(self, horaInicio):
        self.__horaInicio = horaInicio

    @property
    def horaFim(self):
        return self.__horaFim

    @horaFim.setter
    def horaFim(self, horaFim):
        self.__horaFim = horaFim

    @property
    def diaInicio(self):
        return self.__diaInicio

    @diaInicio.setter
    def diaInicio(self, diaInicio):
        self.__diaFim = diaInicio

    @property
    def diaFim(self):
        return self.__diaFim

    @diaFim.setter
    def diaFim(self, diaFim):
        self.__diaFim = diaFim

    @property
    def curso(self):
        return self.__curso

    @curso.setter
    def curso(self, curso):
        self.__curso = curso

    @property
    def filial(self):
        return self.__filial

    @filial.setter
    def filial(self, filial):
        self.__filial = filial

    @property
    def idInstrutor(self):
        return self.__idInstrutor

    @idInstrutor.setter
    def idInstrutor(self, idInstrutor):
        self.__idInstrutor = idInstrutor
