from src.model.conhecimentos_pessoais.pessoa import Pessoa
from src.controllers.pessoas_controller import PessoasControllers
from src.utils.json_utils import serialize
from mapadeconhecimento import app
from flask import request,jsonify
import json

pessoas_controller = PessoasControllers()

@app.route('/pessoas',methods=['GET'])
def obter_pessoas():
    
    nome = request.args.get('nome')

    if not nome :
        return response_webservices_api(pessoas_controller.obter_todas_pessoas_cadastradas())
    else : 
        return response_webservices_api(pessoas_controller.obter_pessoa_por_nome(nome))  

@app.route('/pessoas',methods=['POST'])
def salvar_pessoa():
    
    return response_webservices_api(pessoas_controller.salvar_pessoa(Pessoa(request.get_json())))


def response_webservices_api(response,http_status_code : int = 200,mimetype : str = 'application/json'):
    return jsonify(json.loads(json.dumps(response,default=serialize)))