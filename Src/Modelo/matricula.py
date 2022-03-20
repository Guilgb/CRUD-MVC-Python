from aluno import Aluno
from turma import Turma


class Matricula:
    def __init__(self, idMatricula, aluno: Aluno, turma: Turma):
        self.__matricula = idMatricula
        self.__aluno = aluno
        self.__turma = turma

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula

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
