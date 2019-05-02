class Empresa:

    def __init__(self, nome):
        self._nome = nome

    @property
    def nome(self) -> str:
        return self._nome