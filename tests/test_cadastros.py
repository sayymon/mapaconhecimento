# -*- coding: utf-8 -*-

import pytest
import datetime
import json
 
from datetime import date
from datetime import time

from src.model.conhecimentos_pessoais.pessoa import Pessoa
from src.model.habilidades.tipo_habilidade import TipoHabilidade
from src.model.habilidades.habilidade import Habilidade
from src.model.conhecimentos_pessoais.area_de_conhecimento import AreaDeConhecimento
from src.model.estudos.estudo import Estudo
from src.model.estudos.tipo_estudo import TipoEstudo
from src.model.estudos.status_estudo import StatusEstudo
from src.model.experiencias_de_vida.tipo_experiencia import TipoExperienciaDeVida
from src.model.profissional.cargo import Cargo
from src.model.profissional.empresa import Empresa
from src.utils.json_utils import serialize
from src.dao.conhecimentos_pessoais_dao import ConhecimentosPessoaisDao
from tests.test_instancias_e_dependencias import TestInstanciasEDependencias

class TestCadastros:

    @pytest.fixture
    def test_instancias_e_dependencias(self):
        return TestInstanciasEDependencias()

    def test_criando_uma_pessoa(self, test_instancias_e_dependencias : TestInstanciasEDependencias):
        pessoa_dao = test_instancias_e_dependencias.pessoa_dao
        saymon = pessoa_dao.adicionar_pessoa(test_instancias_e_dependencias.saymon)
        
        assert saymon.id is not None
        assert saymon.nome == "Saymon dos Santos Silva"


    def test_adicionando_habilidades(self,test_instancias_e_dependencias : TestInstanciasEDependencias ):
        pessoa_dao = test_instancias_e_dependencias.pessoa_dao
        saymon = pessoa_dao.adicionar_pessoa(test_instancias_e_dependencias.saymon)

        habilidade_programador_java = test_instancias_e_dependencias.habilidade_programador_java
        habilidade_programador_python = test_instancias_e_dependencias.habilidade_programador_python

        habilidades_dao = test_instancias_e_dependencias.habilidades_dao
        habilidades_dao.adicionar_habilidades(saymon,[habilidade_programador_java,habilidade_programador_python])

        assert len(saymon.habilidades) == 2
        assert saymon.habilidades[0] == habilidade_programador_java
        assert saymon.habilidades[1] == habilidade_programador_python

    def test_adicionando_estudos_ensino_fundamental(self, test_instancias_e_dependencias : TestInstanciasEDependencias):

        pessoa_dao = test_instancias_e_dependencias.pessoa_dao
        saymon = pessoa_dao.adicionar_pessoa(test_instancias_e_dependencias.saymon)

        status_estudo_concluido = StatusEstudo(StatusEstudo.CONCLUIDO)
        tipo_experiencia_estudo = TipoExperienciaDeVida(TipoExperienciaDeVida.ESTUDO)
        test_instancias_e_dependencias.adicionar_experiencias_de_estudos(saymon,status_estudo_concluido, TipoEstudo.ENSINO_FUNDAMENTAL, 9 ,"º Serie",1999)
        
        experiencias_estudo_ensino_fundamental = tipo_experiencia_estudo.filtrar(saymon.experiencias_de_vida, TipoEstudo.ENSINO_FUNDAMENTAL)
        
        print(json.dumps(saymon,default=serialize).encode('utf8'))

        assert len(experiencias_estudo_ensino_fundamental) == 8


    def test_adicionando_estudos_ensino_medio(self, test_instancias_e_dependencias : TestInstanciasEDependencias):

        pessoa_dao = test_instancias_e_dependencias.pessoa_dao
        saymon = pessoa_dao.adicionar_pessoa(test_instancias_e_dependencias.saymon)

        status_estudo_concluido = StatusEstudo(StatusEstudo.CONCLUIDO)
        tipo_experiencia_estudo = TipoExperienciaDeVida(TipoExperienciaDeVida.ESTUDO)

        test_instancias_e_dependencias.adicionar_experiencias_de_estudos(saymon,status_estudo_concluido, TipoEstudo.ENSINO_MEDIO, 4 ,"º Ano",2007)
        
        assert len(tipo_experiencia_estudo.filtrar(saymon.experiencias_de_vida
                                                  ,TipoEstudo.ENSINO_MEDIO)) == 3

    def test_adicionando_estudos_ensino_superior(self, test_instancias_e_dependencias : TestInstanciasEDependencias):

        pessoa_dao = test_instancias_e_dependencias.pessoa_dao
        saymon = pessoa_dao.adicionar_pessoa(test_instancias_e_dependencias.saymon)

        status_estudo_concluido = StatusEstudo(StatusEstudo.CONCLUIDO)
        tipo_experiencia_estudo = TipoExperienciaDeVida(TipoExperienciaDeVida.ESTUDO)
        tipo_estudo_ensino_superior = TipoEstudo(TipoEstudo.ENSINO_SUPERIOR)
        conhecimentos_adquiridos = []
        analise_desenv_de_sistemas = Estudo("Analise e Desenvolvimento de Sistemas"
                                           ,tipo_estudo_ensino_superior
                                           ,status_estudo_concluido
                                           ,datetime.date(2010,6,1)
                                           ,datetime.date(2013,12,11)
                                           ,conhecimentos_adquiridos)

        experiencias_de_vida_dao = test_instancias_e_dependencias.experiencias_de_vida_dao
        experiencias_de_vida_dao.adicionar_experiencias_de_vida(saymon,[analise_desenv_de_sistemas])

        experiencias_estudo_ensino_superior = tipo_experiencia_estudo.filtrar(saymon.experiencias_de_vida,TipoEstudo.ENSINO_SUPERIOR)
        
        assert len(experiencias_estudo_ensino_superior) == 1

    def test_adicionando_profissoes(self, test_instancias_e_dependencias : TestInstanciasEDependencias):
        
        pessoa_dao = test_instancias_e_dependencias.pessoa_dao
        saymon = pessoa_dao.adicionar_pessoa(test_instancias_e_dependencias.saymon)
        
        habilidade_analista_de_sistemas = test_instancias_e_dependencias.habilidade_analista_de_sistemas
        habilidade_programador_informix_4gl = test_instancias_e_dependencias.habilidade_programador_informix_4gl
        habilidade_programador_java = test_instancias_e_dependencias.habilidade_programador_java

        meta_consultoria = Empresa("Grupo Meta Consultoria")
        inicio_experiencia_meta = datetime.date(2011, 8, 10) 
        competencias_exercidas_meta = [habilidade_analista_de_sistemas, habilidade_programador_informix_4gl]
        analista_programador_informix_4gl = Cargo("Analista de Sistemas Programador Informix 4gl" ,inicio_experiencia_meta ,competencias_exercidas_meta, meta_consultoria)

        porto_seguro = Empresa("Porto Seguro Cia")
        inicio_experiencia_porto_seguro = datetime.date(2011, 2, 4) 
        competencias_exercidas_porto_seguro = [habilidade_analista_de_sistemas, habilidade_programador_java]
        analista_programador_java = Cargo("Analista de Sistemas Programador" ,inicio_experiencia_porto_seguro ,competencias_exercidas_porto_seguro, porto_seguro)

        experiencias_de_vida_dao = test_instancias_e_dependencias.experiencias_de_vida_dao

        experiencias_de_vida_dao.adicionar_experiencias_de_vida(saymon,[analista_programador_informix_4gl,analista_programador_java])

        tipo_experiencia_profissional = TipoExperienciaDeVida(TipoExperienciaDeVida.PROFISSIONAL)

        experiencias_profissionais = tipo_experiencia_profissional.filtrar(saymon.experiencias_de_vida)

        print(json.dumps(saymon,default=serialize))

        assert len(experiencias_profissionais) == 2       

