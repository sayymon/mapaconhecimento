from src.model.conhecimentos_pessoais.pessoa import Pessoa
from src.model.habilidades.habilidade import Habilidade
from src.model.habilidades.tipo_habilidade import TipoHabilidade
from src.model.conhecimentos_pessoais.conhecimento import Conhecimento
from src.model.conhecimentos_pessoais.area_de_conhecimento import AreaDeConhecimento

from src.dao.conhecimentos_pessoais_dao import ConhecimentosPessoaisDao 
from src.dao.habilidades_dao import HabilidadesDao
from src.dao.experiencias_de_vida_dao import ExperienciasDeVidaDao

from pymongo.database import Database,Collection
from bson.objectid import ObjectId

from src.utils import json_utils
from typing import List

class PessoaDao:

    def __init__(self):
        self.conhecimentos_pessoais_dao = ConhecimentosPessoaisDao()
        self.conhecimentos_pessoais_collection = self.conhecimentos_pessoais_dao.conhecimentos_pessoais_collection
        self.habilidades_dao = HabilidadesDao()
        self.experiencias_de_vida_dao = ExperienciasDeVidaDao()

    def adicionar_pessoa(self ,pessoa : Pessoa) -> Pessoa:
        pessoa_db = self.find_pessoa(pessoa)

        if not pessoa_db:
            pessoa_json = json_utils.obj_to_json(pessoa)

            pessoa_db = self.conhecimentos_pessoais_collection.insert_one(pessoa_json)

            pessoa.id = pessoa_db.inserted_id
        else:
            pessoa.id = str(pessoa_db.id)

        return pessoa

    def find_pessoa(self,pessoa : Pessoa) -> Pessoa:
        pessoa_db = None
        filter_pessoa = None

        if hasattr(pessoa,"_id") and pessoa.id :
            filter_pessoa = {"_id" : ObjectId(pessoa.id)}
        elif pessoa.nome :
            filter_pessoa = {"nome" : pessoa.nome}
        
        collect_pessoa = self.conhecimentos_pessoais_collection.find_one(filter_pessoa)
        if collect_pessoa :
            pessoa_db =  self.collect_to_object(collect_pessoa)

        return pessoa_db

    def find_pessoas_por_nome(self,nome : str) -> List[Pessoa] :
        pessoas = []

        filter_pessoa = {"nome" : { "$regex" : nome }}
        
        collections_pessoa_result = self.conhecimentos_pessoais_collection.find(filter_pessoa)        

        for collect_pessoa in collections_pessoa_result:
            pessoas.append(self.collect_to_object(collect_pessoa))

        return pessoas

    def find_all_pessoas(self,limite = 10,skip = 0) -> List[Pessoa]:
        pessoas = []
        collect_pessoas = self.conhecimentos_pessoais_collection.find().limit(limite).skip(skip)
        for collect_pessoa in collect_pessoas :
            pessoas.append(self.collect_to_object(collect_pessoa))

        return pessoas

    def collect_to_object(self,collect_pessoa : Collection ) -> Pessoa:
        
        pessoa = Pessoa(collect_pessoa["nome"])
        pessoa.id = str(collect_pessoa['_id'])

        habilidades = self.habilidades_dao.collect_to_list_object(collect_pessoa.get('habilidades'))
        pessoa.habilidades.extend(habilidades)        
        
        experiencias_de_vida = self.experiencias_de_vida_dao.collect_to_list_object(collect_pessoa.get('experiencias_de_vida'))
        pessoa.experiencias_de_vida.extend(experiencias_de_vida)

        return pessoa
   



