class TipoHabilidade:

    FISICAS_E_MOTORAS = "Fisicas e Motoras"
    INTELECTUAIS_E_TECNICAS = "Intelectuais e Tecnicas"
    COMPORTAMENTAIS = "Comportamentais"

    def __init__(self, nome):
        self._nome = nome

    @property
    def nome(self) -> str:
        return self._nome

    def __hash__(self):
        return hash(self.nome)

    def __eq__(self,other):
        return (self.__class__ == other.__class__ and
                self.nome == other.nome
               )        