from area import Area


class Curso:
    def __init__(self, curso: str, chCurso: str, area: Area) -> None:
        self.__curso = curso
        self.__chCurso = chCurso
        self.__areas = area

    def insereArea(self, area: Area):
        listaAreas = []
        listaAreas.append(area.area)

    def listaArea(self):
        for area in self.listaAreas:
            print(area)

    @property
    def curso(self):
        return self.__curso

    @curso.setter
    def curso(self, curso):
        self.__curso = curso

    @property
    def chCurso(self):
        return self.__chCurso

    @chCurso.setter
    def chCurso(self, chCurso):
        self.__chCurso = chCurso

    @property
    def areas(self):
        return self.__areas

    @areas.setter
    def areas(self, areas):
        self.__areas = areas
