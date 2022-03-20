from estado import Estado


class Cidade:
    def __init__(self, cidade: str):
        self.__cidade = cidade
        self.__estados = Estado

    def inserirEstado(self, estado: Estado):
        self.__estados = estado.estado

    @property
    def cidade(self):
        return self.__cidade

    @cidade.setter
    def cidade(self, cidade):
        self.__cidade = cidade

    @property
    def estado(self):
        return self.__estados

    @estado.setter
    def estado(self, estado):
        self.__estados = estado
