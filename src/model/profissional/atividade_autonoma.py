from src.model.profissional.profissional import Profissional

from datetime import date

class AtividadeAutonoma(Profissional) :

    def __init__(self, nome, data_inicio : date, competencias_exercidas : list):
        super().__init__(nome, data_inicio, competencias_exercidas)