from flask import render_template, url_for, request, flash, redirect
from comunidadeImpressionadora import app, database, bcrypt
from comunidadeImpressionadora.forms import FormCriarConta, FormLogin
from comunidadeImpressionadora.models import Usuario

lista_usuarios = ['lira', 'Alon', 'Alessandra', 'Bia']

@app.route("/")
def home():
    return render_template('home.html')


@app.route("/contato")
def contatos():
    return render_template('contato.html')


@app.route("/usuarios")
def usuarios():
    return render_template('usuarios.html', lista_usuarios = lista_usuarios)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form_login = FormLogin()
    form_criar_conta = FormCriarConta()

    if form_login.validate_on_submit() and 'botao_submit_login' in request.form:
        flash(f'Login feito com sucesso no e-mail: {form_login.email.data}', 'alert-success')
        return redirect(url_for('home'))
    if form_criar_conta.validate_on_submit() and 'botao_submit_criar_conta' in request.form:
        senha_crypt = bcrypt.generate_password_hash(form_criar_conta.senha.data)
        usuario = Usuario(username = form_criar_conta.username.data, email = form_criar_conta.email.data, senha = senha_crypt)
        database.session.add(usuario)
        database.session.commit()
        flash(f'Conta criada com sucesso para o e-mail: {form_criar_conta.email.data}', 'alert-success')
        return redirect(url_for('home'))

    return render_template('login.html', form_login = form_login, form_criar_conta = form_criar_conta)