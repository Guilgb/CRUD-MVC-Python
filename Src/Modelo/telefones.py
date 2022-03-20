class Telefones:
    def __init__(self, numeroTelefone: str) -> None:
        self.__numeroTelefone = numeroTelefone

    @property
    def numeroTelefone(self):
        return self.__numeroTelefone

    @numeroTelefone.setter
    def numeroTelefone(self, numeroTelefone):
        self.numeroTelefone = numeroTelefone
