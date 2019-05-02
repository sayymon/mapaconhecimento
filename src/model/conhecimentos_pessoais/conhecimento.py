class Conhecimento:

    def __init__(self, nome, area_de_conhecimento : list) :
        self._nome = nome 
        self._area_de_conhecimento = area_de_conhecimento

    @property
    def nome(self):
        return self._nome

    def area_de_conhecimento(self):
        return self._area_de_conhecimento

    def __eq__(self,other):
         return (
                self.__class__ == other.__class__ and
                self.nome == other.nome and
                self.area_de_conhecimento == other.area_de_conhecimento
                )