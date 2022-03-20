class Filial:
    def __init__(self, nomeFilial: str, localidade: str) -> None:
        self.__nomeFilial = nomeFilial
        self.__localidade = localidade

    @property
    def nomeFilial(self):
        return self.__nomeFilial

    @nomeFilial.setter
    def nomeFilial(self, nomeFilial):
        self.__nomeFilial = nomeFilial

    @property
    def localidade(self):
        return self.__localidade

    @localidade.setter
    def localidade(self, localidade):
        self.__localidade = localidade
