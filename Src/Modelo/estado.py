class Estado:
    def __init__(self, estado: str) -> None:
        self.__estado = estado

    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, estado):
        self.__estado = estado
