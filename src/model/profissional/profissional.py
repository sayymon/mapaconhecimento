from src.model.experiencias_de_vida.tipo_experiencia import TipoExperienciaDeVida
from src.model.experiencias_de_vida.experiencia_de_vida import ExperienciaDeVida

from datetime import date

class Profissional(ExperienciaDeVida):

    def __init__(self, nome, data_inicio : date, competencias_exercidas : list,data_fim : date = None):
        tipo_experiencia_profissional = TipoExperienciaDeVida(TipoExperienciaDeVida.PROFISSIONAL)
        super().__init__(nome, tipo_experiencia_profissional, data_inicio,data_fim)
        self._competencias_exercidas = competencias_exercidas

    @property
    def competencias_exercidas(self) -> list:
        return self._competencias_exercidas