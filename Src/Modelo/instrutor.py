from src.modelo.Pessoa import Pessoa
from src.modelo.Telefones import Telefones
from src.modelo.Cidade import Cidade


class Instrutor(Pessoa):
    def __init__(self, nomePessoa: str, telefone: Telefones, cidade: Cidade,
                 formacao: str):
        super().__init__(nomePessoa, telefone, cidade)
        self.__formacao = formacao

    @property
    def formacao(self):
        return self.__formacao

    @formacao.setter
    def formacao(self, formacao):
        self.__formacao = formacao
