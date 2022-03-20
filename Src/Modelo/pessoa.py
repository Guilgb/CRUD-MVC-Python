import abc
from cidade import Cidade
from telefones import Telefones


class Pessoa(abc.ABC):
    def __init__(self, nomePessoa: str, telefone: Telefones, cidade: Cidade):
        self.__nomePessoa = nomePessoa
        self.__telefones = telefone
        self.__cidades = cidade

    def insereCidade(self, cidade: Cidade):
        listaCidades = []
        listaCidades.append((cidade.cidade, cidade.estado))

    def listaCidade(self):
        for cidade in self.listacidades:
            print(cidade.cidade, cidade.estado)

    def insereTelefone(self, telefone: Telefones):
        listaTelefones = []
        listaTelefones.append(telefone.numeroTelefone)

    def listaTelefone(self):
        for telefone in self.listaTelefones:
            print(telefone)

    @property
    def nomePessoa(self):
        return self.__nomePessoa

    @nomePessoa.setter
    def nomePessoa(self, nomePessoa):
        self.__nomePessoa = nomePessoa

    @property
    def telefones(self):
        return self.__telefones

    @telefones.setter
    def telefones(self, telefones):
        self.__telefones = telefones

    @property
    def cidades(self):
        return self.__cidades

    @cidades.setter
    def cidades(self, cidade):
        self.__cidades = cidade
