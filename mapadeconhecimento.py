from flask import Flask

app = Flask(__name__)

#Configuracoes isoladas em um arquivo de configuracoes em python
app.config.from_pyfile('config/config.py')

from src.webservices import *

if __name__ == '__main__':
    app.run(debug=True)
