class Escolaridade:
    def __init__(self, escolaridade: str) -> None:
        self.__escolaridade = escolaridade

    @property
    def escolaridade(self):
        return self.__escolaridade

    @escolaridade.setter
    def escolaridade(self, escolariade):
        self.__escolaridade = escolariade
