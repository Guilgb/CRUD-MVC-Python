from src.modelo.Pessoa import Pessoa
from src.modelo.Telefones import Telefones
from src.modelo.Cidade import Cidade
from src.modelo.Escolaridade import Escolaridade


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
