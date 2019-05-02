class TipoEstudo:

    ENSINO_FUNDAMENTAL = 'Ensino Fundamental'
    ENSINO_MEDIO = 'Ensino Medio'
    ENSINO_SUPERIOR = 'Ensino Superior'
    CURSOS_E_ESPECIALIZACOES = 'Cursos e Especializações'

    def __init__(self, nome):
        self._nome = nome

    @property
    def nome(self) -> str:
        return self._nome
