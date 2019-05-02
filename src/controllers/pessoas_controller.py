from src.model.conhecimentos_pessoais.pessoa import Pessoa

from src.dao.pessoa_dao import PessoaDao

class PessoasControllers:

    def __init__(self):
        self._pessoa_dao = PessoaDao()

    def obter_todas_pessoas_cadastradas(self):
        return self._pessoa_dao.find_all_pessoas()

    def obter_pessoa_por_nome(self,nome : str):
        return self._pessoa_dao.find_pessoas_por_nome(nome)

    def salvar_pessoa(self,pessoa : Pessoa):
        return self._pessoa_dao.adicionar_pessoa(pessoa)