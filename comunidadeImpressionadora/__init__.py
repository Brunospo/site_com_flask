from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

token = 'REMOVIDO'
app.secret_key = token
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'

database = SQLAlchemy(app)

from comunidadeImpressionadora import routes