from aluno import Aluno
from turma import Turma


class Matricula:
    def __init__(self, aluno: str, turma: str):
        self.__aluno = aluno
        self.__turma = turma

    @property
    def aluno(self):
        return self.__aluno

    @aluno.setter
    def aluno(self, aluno):
        self.__aluno = aluno

    @property
    def turma(self):
        return self.__turma

    @turma.setter
    def turma(self, turma):
        self.__turma = turma
