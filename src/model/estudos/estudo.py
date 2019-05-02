from src.model.experiencias_de_vida.experiencia_de_vida import ExperienciaDeVida
from src.model.estudos.tipo_estudo import TipoEstudo
from src.model.estudos.status_estudo import StatusEstudo
from src.model.experiencias_de_vida.tipo_experiencia import TipoExperienciaDeVida

from datetime import date

class Estudo(ExperienciaDeVida):

    def __init__(self, nome, tipo_estudo: TipoEstudo, status: StatusEstudo, data_inicio: date, data_fim: date, conhecimentos_adquiridos):
        tipo_experiencia_estudo = TipoExperienciaDeVida(TipoExperienciaDeVida.ESTUDO) 
        super().__init__(nome, tipo_experiencia_estudo, data_inicio, data_fim)
        self._tipo_estudo = tipo_estudo
        self._status = status
        self._conhecimentos_adquiridos = conhecimentos_adquiridos 

    @property
    def tipo_estudo(self) -> TipoEstudo:
        return self._tipo_estudo

    @property
    def status(self) -> StatusEstudo:
        return self._tipo

    def __str__(self):
        return f'Nome : {self.nome}'\
               f'Tipo : {self.tipo_estudo}'\
               f'Status :{self.status}'    