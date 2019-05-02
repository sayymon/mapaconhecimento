from src.model.habilidades.habilidade import Habilidade
from src.model.experiencias_de_vida.experiencia_de_vida import ExperienciaDeVida
from src.model.experiencias_de_vida.tipo_experiencia import TipoExperienciaDeVida
from src.model.estudos.estudo import Estudo

class Pessoa:

    def __init__(self, nome, habilidades: list = None, experiencias_de_vida: list = None,json : dict = None):
        if not json :
            self._id = None
            self._nome = nome
            self._habilidades = habilidades
            self._experiencias_de_vida = experiencias_de_vida
        else:
            self.__dict__.update(json)  

    def __str__(self):
        return f'Nome:{self.nome} - ' \
               f'Habilidades ; {self.habilidades} - ' \
               f'Experiencias de Vida: {self.experiencias_de_vida}'

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, nome : str):
        self._nome = nome

    @property
    def habilidades(self) -> list:
        if not self._habilidades:
            self._habilidades = []

        return self._habilidades


    @property
    def experiencias_de_vida(self, tipo_experiencia : str = None) -> list:
        if not self._experiencias_de_vida:
            self._experiencias_de_vida = []

        if not tipo_experiencia:
            return self._experiencias_de_vida