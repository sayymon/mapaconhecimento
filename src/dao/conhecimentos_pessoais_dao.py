from src.model.conhecimentos_pessoais.pessoa import Pessoa
from src.model.conhecimentos_pessoais.area_de_conhecimento import AreaDeConhecimento
from src.model.conhecimentos_pessoais.conhecimento import Conhecimento
from src.model.habilidades.habilidade import Habilidade
from src.model.estudos.estudo import Estudo

from pymongo.database import Database,Collection
from bson.objectid import ObjectId

from src.utils import json_utils

import pymongo

class ConhecimentosPessoaisDao:
    
    #Implementacao de Singleton
    class __ConhecimentosPessoaisDao:
        def __init__(self):
            print("Conectando no banco")
            mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
            print("Creando o Database")
            self._mapa_conhecimentos_pessoais_db = mongo_client["mapaConhecimentosPessoais"]            
        
        @property
        def mapa_conhecimentos_pessoais_db(self) -> Database:
            return self._mapa_conhecimentos_pessoais_db

        def __str__(self):
            return repr(self)

    instance = None

    def __init__(self):
        if not ConhecimentosPessoaisDao.instance:
            ConhecimentosPessoaisDao.instance = ConhecimentosPessoaisDao.__ConhecimentosPessoaisDao()

    def __getattr__(self, name):
        return getattr(self.instance, name)
    
    @property
    def conhecimentos_pessoais_collection(self) -> Collection:
        return self.instance.mapa_conhecimentos_pessoais_db["conhecimentosPessoais"]


    def collect_to_list_object(self, collect_conhecimentos):
        conhecimentos = []

        if collect_conhecimentos : 
            for collect_conhecimento in collect_conhecimentos : 
                conhecimento = None
                nome_conhecimento = collect_conhecimento["nome"]
                areas_de_conhecimento = self.collect_to_list_object(collect_conhecimento.get("area_de_conhecimento"))

                if "conhecimentos" in collect_conhecimento: 
                    conhecimentos_area_de_conhecimentos = self.collect_to_list_object(collect_conhecimento["conhecimentos"])
                    conhecimento = AreaDeConhecimento(nome_conhecimento,areas_de_conhecimento,conhecimentos_area_de_conhecimentos)
                else:
                    conhecimento = Conhecimento(nome_conhecimento,areas_de_conhecimento)

                conhecimentos.append(conhecimento)
        
        return conhecimentos