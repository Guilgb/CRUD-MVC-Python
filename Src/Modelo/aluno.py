from pessoa import Pessoa
from telefones import Telefones
from cidade import Cidade
from escolaridade import Escolaridade


class Aluno(Pessoa):
    def __init__(self, nomePessoa: str, telefone: Telefones, cidade: Cidade,
                 escolaridade: Escolaridade):
        super().__init__(nomePessoa, telefone, cidade)
        self.__escolaridades = escolaridade

    def inserirEscolaridade(self, escolaridade: Escolaridade):
        listaEscolaridades = []
        listaEscolaridades.append(escolaridade.escolaridade)

    def listaEscolaridade(self):
        for escolaridade in self.listaEscolaridades:
            print(escolaridade)

    @property
    def escolaridades(self):
        return self.__escolaridades

    @escolaridades.setter
    def escolaridades(self, escolaridade):
        self.__escolaridades = escolaridade
