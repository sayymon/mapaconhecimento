# -*- coding: utf-8 -*-

import pytest
import datetime

from src.model.conhecimentos_pessoais.pessoa import Pessoa
from src.model.habilidades.tipo_habilidade import *
from src.model.habilidades.habilidade import *
from src.model.conhecimentos_pessoais.area_de_conhecimento import AreaDeConhecimento
from src.model.estudos.estudo import Estudo
from src.model.estudos.tipo_estudo import TipoEstudo
from src.model.estudos.status_estudo import StatusEstudo
from src.model.experiencias_de_vida.tipo_experiencia import TipoExperienciaDeVida
from src.model.profissional.cargo import Cargo
from src.model.profissional.empresa import Empresa

from src.dao.pessoa_dao import PessoaDao
from src.dao.experiencias_de_vida_dao import ExperienciasDeVidaDao
from src.dao.habilidades_dao import HabilidadesDao


class TestInstanciasEDependencias:

    @property    
    def saymon(self) -> Pessoa:
        return Pessoa("Saymon dos Santos Silva")

    @property
    def linguagem_de_programacao(self):
        return AreaDeConhecimento("Linguagem de Programação")

    @property
    def logica_de_programacao(self):
        return AreaDeConhecimento("Logica de Programação")

    @property
    def programacao_estruturada(self):         
        return AreaDeConhecimento("Programação Estruturada")
    
    @property
    def programacao_orientada_a_objetos(self):         
        return AreaDeConhecimento("Programação Orientada a Objetos")

    @property
    def tipo_habilidade_intelectual_e_tecnicas(self):
        return TipoHabilidade(TipoHabilidade.INTELECTUAIS_E_TECNICAS)

    @property
    def habilidade_analista_de_sistemas(self):
        conhecimentos_analista_sistemas = []
        return Habilidade("Analista de Sistemas",self.tipo_habilidade_intelectual_e_tecnicas , conhecimentos_analista_sistemas)    

    @property
    def habilidade_programador_informix_4gl(self):
        return Habilidade("Programador Informix 4gl"
                         ,self.tipo_habilidade_intelectual_e_tecnicas
                         ,self.conhecimentos_programador_informix_4gl)

    @property
    def habilidade_programador_java(self):
        return Habilidade("Programador Java"
                         ,self.tipo_habilidade_intelectual_e_tecnicas
                         ,self.conhecimentos_programador_java)

    @property
    def habilidade_programador_python(self):
        return Habilidade("Programador Python"
                         ,self.tipo_habilidade_intelectual_e_tecnicas
                         ,self.conhecimentos_programador_python)

    @property
    def conhecimentos_programador_java(self):        
        java = AreaDeConhecimento("Java",[self.linguagem_de_programacao],[self.logica_de_programacao,self.programacao_orientada_a_objetos,AreaDeConhecimento("FrameWorks Java")])
        return [java] 

    @property
    def conhecimentos_programador_informix_4gl(self):
        informix_4gl = AreaDeConhecimento("Informix 4gl",[self.linguagem_de_programacao],[self.logica_de_programacao,self.programacao_estruturada,AreaDeConhecimento("Programação Funcional")])
        return [informix_4gl] 

    @property
    def conhecimentos_programador_python(self):
        python = AreaDeConhecimento("Python",[self.linguagem_de_programacao],[self.logica_de_programacao,self.programacao_orientada_a_objetos,AreaDeConhecimento("FrameWorks Python")])
        return [python]

    @property
    def pessoa_dao(self) -> PessoaDao:
        return PessoaDao()

    @property
    def experiencias_de_vida_dao(self) -> ExperienciasDeVidaDao:
        return ExperienciasDeVidaDao()

    @property
    def habilidades_dao(self) -> HabilidadesDao:
        return HabilidadesDao()

    def adicionar_experiencias_de_estudos(self, pessoa, status_estudo_concluido, nome_tipo_estudo : str, anos : int ,nome_estudo, ano_inicio : int ):
        estudos = []
        tipo_estudo = TipoEstudo(nome_tipo_estudo)
        for serie in range(1,anos):
            nome_estudo_serie = f"{serie}" + nome_estudo 
            estudo = Estudo(nome_estudo_serie
                                 ,tipo_estudo
                                 ,status_estudo_concluido
                                 ,datetime.date(ano_inicio,2,1)
                                 ,datetime.date(ano_inicio+1,2,1)
                                 ,[])
            
            estudos.append(estudo)

            
            ano_inicio =+ 1
        
        self.experiencias_de_vida_dao.adicionar_experiencias_de_vida(pessoa,estudos)
