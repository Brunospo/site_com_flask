from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)

token = 'REMOVIDO'
app.secret_key = token
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'

database = SQLAlchemy(app)

bcrypt = Bcrypt(app)

from comunidadeImpressionadora import routes