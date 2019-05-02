from src.model.conhecimentos_pessoais.conhecimento import Conhecimento

class AreaDeConhecimento(Conhecimento):

    def __init__(self, nome,areas_de_conhecimentos : list = None, conhecimentos : list = None):
        super().__init__(nome,areas_de_conhecimentos)
        self._nome = nome
        self._conhecimentos = conhecimentos
    
    @property
    def conhecimentos(self):
        if not self._conhecimentos:
            self._conhecimentos = []

        return self._conhecimentos
