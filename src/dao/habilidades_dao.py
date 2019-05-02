from src.model.conhecimentos_pessoais.pessoa import Pessoa
from src.model.conhecimentos_pessoais.conhecimento import Conhecimento
from src.model.conhecimentos_pessoais.area_de_conhecimento import AreaDeConhecimento
from src.dao.conhecimentos_pessoais_dao import ConhecimentosPessoaisDao 
from src.model.habilidades.tipo_habilidade import TipoHabilidade
from src.model.habilidades.habilidade import Habilidade

from pymongo.database import Database,Collection
from bson.objectid import ObjectId

from src.utils import json_utils

class HabilidadesDao:

    def __init__(self):
        self.conhecimentos_pessoais_dao = ConhecimentosPessoaisDao()
        self.conhecimentos_pessoais_collection = self.conhecimentos_pessoais_dao.conhecimentos_pessoais_collection

    def adicionar_habilidades(self,pessoa : Pessoa, habilidades : list):
        if habilidades and pessoa.id:
            habilidades_json = json_utils.obj_to_json(habilidades)
            self.conhecimentos_pessoais_collection.update_one({ "_id" : ObjectId(pessoa.id)}
                                                             ,{ "$addToSet": { "habilidades" : { "$each" : habilidades_json}}}
                                                             ,)
            pessoa.habilidades.extend(habilidades)

    def find_habilidades_por_nome(self,nome_habilidade : str) -> set: 
        habilidades = set()

        if nome_habilidade:
           collect_pessoas = self.conhecimentos_pessoais_collection.find({ "habilidades.nome" : { "$regex" : nome_habilidade }})
           for collect_pessoa in collect_pessoas:
               habilidades.update(self.collect_to_list_object(collect_pessoa.get('habilidades')))

        return habilidades

    def find_habilidades_por_tipo(self,tipo_habilidade : TipoHabilidade) -> set: 
        habilidades = set()

        if tipo_habilidade:
           collect_pessoas = self.conhecimentos_pessoais_collection.find({ "habilidades.tipo.nome" : tipo_habilidade.nome})
           for collect_pessoa in collect_pessoas:
               habilidades.update(self.collect_to_list_object(collect_pessoa.get('habilidades')))

        return habilidades

    def find_habilidades_por_conhecimento(self, conhecimento: Conhecimento) -> set:
        habilidades = set()

        if conhecimento:
           collect_pessoas = self.conhecimentos_pessoais_collection.find({"$or": [
               {"habilidades.conhecimentos.nome": conhecimento.nome},
               {"habilidades.conhecimentos.conhecimentos.nome": conhecimento.nome},
               {"habilidades.conhecimentos.conhecimentos.conhecimentos.nome": conhecimento.nome}
           ]
           })

           for collect_pessoa in collect_pessoas:
                habilidades_pessoa = self.collect_to_list_object(
                    collect_pessoa.get('habilidades'))
                for habilidade_pessoa in habilidades_pessoa:
                    if self.is_conhecimento_in_conhecimentos(conhecimento, habilidade_pessoa.conhecimentos):
                        habilidades.add(habilidade_pessoa)

        return habilidades

    def is_conhecimento_in_conhecimentos(self,conhecimento : Conhecimento, conhecimentos : list):
        is_conhecimento_in_conhecimentos = False

        for conhecimento_habilidade in conhecimentos:
            if conhecimento_habilidade.nome == conhecimento.nome:
                is_conhecimento_in_conhecimentos = True
                break
            elif (isinstance(conhecimento_habilidade,AreaDeConhecimento) and  
                  conhecimento_habilidade.conhecimentos and
                  len(conhecimento_habilidade.conhecimentos) > 0 and
                  self.is_conhecimento_in_conhecimentos(conhecimento,conhecimento_habilidade.conhecimentos)):
                is_conhecimento_in_conhecimentos = True
                break
        return is_conhecimento_in_conhecimentos

    def collect_to_list_object(self, collect_habilidades):
        habilidades = set()
        
        if collect_habilidades : 
            for collect_habilidade in collect_habilidades:

                nome = collect_habilidade["nome"]
                tipo = TipoHabilidade(collect_habilidade.get("tipo")["nome"])
                conhecimentos = self.conhecimentos_pessoais_dao.collect_to_list_object(collect_habilidade.get("conhecimentos"))

                habilidades.add(Habilidade(nome,tipo,conhecimentos))

        return habilidades            
