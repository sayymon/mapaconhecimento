# -*- coding: utf-8 -*-

import pytest


from src.model.conhecimentos_pessoais.pessoa import Pessoa
from src.model.conhecimentos_pessoais.conhecimento import Conhecimento
from src.model.habilidades.tipo_habilidade import TipoHabilidade

from tests.test_instancias_e_dependencias import TestInstanciasEDependencias

class TestConsultas:

    @pytest.fixture
    def test_instancias_e_dependencias(self):
        return TestInstanciasEDependencias()


    def test_buscar_pessoas_por_nome(self, test_instancias_e_dependencias : TestInstanciasEDependencias):
        
        pessoa_dao = test_instancias_e_dependencias.pessoa_dao

        pessoa_dao.adicionar_pessoa(Pessoa("Kelly Barros dos Santos"))
        pessoa_dao.adicionar_pessoa(Pessoa("Saymon dos Santos Silva"))
        pessoa_dao.adicionar_pessoa(Pessoa("Gabrielly Barros dos Santos"))
        pessoa_dao.adicionar_pessoa(Pessoa("Nicolly Barros dos Santos"))
        
        pessoas = test_instancias_e_dependencias.pessoa_dao.find_pessoas_por_nome("Saymon dos Santos Silva")

        assert len(pessoas) == 1

        pessoas = test_instancias_e_dependencias.pessoa_dao.find_pessoas_por_nome("Santos")

        assert len(pessoas) == 4


    def test_buscar_habilidades_de_uma_pessoa(self, test_instancias_e_dependencias : TestInstanciasEDependencias):

        pessoa = test_instancias_e_dependencias.pessoa_dao.find_pessoa(Pessoa("Saymon dos Santos Silva"))
        
        habilidades = pessoa.habilidades

        assert habilidades 

    def test_buscar_habilidades_por_nome(self, test_instancias_e_dependencias : TestInstanciasEDependencias):

        habilidades = test_instancias_e_dependencias.habilidades_dao.find_habilidades_por_nome("Programador")
        
        assert habilidades     

    def test_buscar_habilidades_por_tipo(self, test_instancias_e_dependencias : TestInstanciasEDependencias):

        habilidades = test_instancias_e_dependencias.habilidades_dao.find_habilidades_por_tipo(TipoHabilidade(TipoHabilidade.INTELECTUAIS_E_TECNICAS))
        
        assert habilidades  

    def test_buscar_habilidades_por_conhecimento(self, test_instancias_e_dependencias : TestInstanciasEDependencias):

        habilidades = test_instancias_e_dependencias.habilidades_dao.find_habilidades_por_conhecimento(Conhecimento("FrameWorks Java",[]))
        
        assert habilidades          