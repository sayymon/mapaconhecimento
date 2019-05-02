from datetime import date

from src.model.experiencias_de_vida.tipo_experiencia import TipoExperienciaDeVida

class ExperienciaDeVida:

    def __init__(self, nome, tipo: TipoExperienciaDeVida, data_inicio: date, data_fim: date = None):
        self._nome = nome
        self._tipo = tipo
        self._data_inicio = data_inicio
        self._data_fim = data_fim


    @property
    def nome(self) -> str:
        return self._nome

    @property
    def tipo(self) -> TipoExperienciaDeVida:
        return self._tipo


    @property
    def data_inicio(self) -> str:
        return self._data_inicio

    @property
    def data_fim(self) -> str:
        return self._data_fim