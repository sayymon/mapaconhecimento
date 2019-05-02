from src.model.profissional.profissional import Profissional
from src.model.profissional.empresa import Empresa

from datetime import date

class Cargo(Profissional) :

    def __init__(self, nome, data_inicio : date, competencias_exercidas : list, empresa : Empresa = None):
        super().__init__(nome, data_inicio, competencias_exercidas)
        self._empresa = empresa

    @property
    def empresa(self) -> Empresa:
        return self._empresa