from src.model.habilidades.tipo_habilidade import TipoHabilidade

class Habilidade:

    def __init__(self, nome, tipo: TipoHabilidade, conhecimentos: list):
        self._nome = nome
        self._tipo = tipo
        self._conhecimentos = conhecimentos

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def tipo(self) -> str:
        return self._tipo

    @property
    def conhecimentos(self) -> list:
        return self._conhecimentos

    def __hash__(self):
        return hash(self.nome) + hash(self.tipo)

    def __eq__(self,other):
        return (self.__class__ == other.__class__ and
                self.nome == other.nome and 
                self.tipo == other.tipo
               )