from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class FormCriarConta(FlaskForm):
  username = StringField('Nome de Usuário', validators=[DataRequired()])
  email = StringField('Email', validators=[DataRequired(), Email()])
  senha = PasswordField('Senha', validators=[DataRequired(), Length(6,20)])
  confirmacao = PasswordField('Confirmação de Senha', validators=[DataRequired(), EqualTo('senha')])
  botao_submit_criar_conta = SubmitField('Criar Conta')

class FormLogin(FlaskForm):
  email = StringField('Email', validators= [DataRequired(), Email()])
  senha = PasswordField('Senha', validators= [DataRequired(), Length(6,20)])
  lembrar_dados = BooleanField('Lembrar Dados de Acesso')
  botao_submit_login = SubmitField('Fazer Login')