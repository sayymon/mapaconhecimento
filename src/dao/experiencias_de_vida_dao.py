from src.model.conhecimentos_pessoais.pessoa import Pessoa

from src.model.estudos.estudo import Estudo
from src.model.estudos.tipo_estudo import TipoEstudo
from src.model.estudos.status_estudo import StatusEstudo 

from src.model.profissional.profissional import Profissional

from src.model.experiencias_de_vida.experiencia_de_vida import ExperienciaDeVida
from src.model.experiencias_de_vida.tipo_experiencia import TipoExperienciaDeVida

from src.dao.conhecimentos_pessoais_dao import ConhecimentosPessoaisDao
from src.dao.habilidades_dao import HabilidadesDao 

from pymongo.database import Database,Collection
from bson.objectid import ObjectId
from typing import List
from src.utils import json_utils

class ExperienciasDeVidaDao:

    def __init__(self):
        self.conhecimentos_pessoais_dao = ConhecimentosPessoaisDao()
        self.conhecimentos_pessoais_collection = self.conhecimentos_pessoais_dao.conhecimentos_pessoais_collection
        self.habilidades_dao = HabilidadesDao()

    def adicionar_experiencias_de_vida(self ,pessoa : Pessoa ,experiencias : list) -> Pessoa:

        if pessoa.id and experiencias:
            experiencias_json = json_utils.obj_to_json(experiencias)
            self.conhecimentos_pessoais_collection.update_many({ "_id" : ObjectId(pessoa.id)}
                                                             ,{ "$addToSet": { "experiencias_de_vida" : { "$each": experiencias_json } } }
                                                             )
            pessoa.experiencias_de_vida.extend(experiencias)

        return pessoa        

    def collect_to_list_object(self,collect_experiencias) -> List[ExperienciaDeVida]:
        experiencias_de_vida = []

        if collect_experiencias:
            for collect_experiencia in collect_experiencias:
                experiencia_de_vida = None
                nome = collect_experiencia.get("nome")
                tipo = TipoExperienciaDeVida(collect_experiencia.get("tipo")["nome"])
                data_inicio = collect_experiencia.get("data_inicio")
                data_fim = collect_experiencia.get("data_fim")

                if tipo.nome == TipoExperienciaDeVida.ESTUDO:
                    tipo_estudo = TipoEstudo(collect_experiencia["tipo_estudo"]["nome"])
                    status_estudo = StatusEstudo(collect_experiencia["status"]["valor"])
                    conhecimentos_adquiridos = self.conhecimentos_pessoais_dao.collect_to_list_object(collect_experiencia.get("conhecimentos_adquiridos"))
                    experiencia_de_vida = Estudo(nome,tipo_estudo,status_estudo,data_inicio,data_fim,conhecimentos_adquiridos)
                elif tipo.nome == TipoExperienciaDeVida.PROFISSIONAL:    
                    competencias_exercidas = self.habilidades_dao.collect_to_list_object(collect_experiencia["competencias_exercidas"])
                    experiencia_de_vida = Profissional(nome,data_inicio,competencias_exercidas,data_fim)
                
                experiencias_de_vida.append(experiencia_de_vida)

        return experiencias_de_vida