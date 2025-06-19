from main import app, database
from models import Usuario, Post

with app.app_context(): # Todos os codigos tem que ter esse contexto

# ---------------------------Criar Banco de Dados---------------------------------------
  database. create_all()

# ---------------------------criar usuario---------------------------------------
#   usuario = Usuario(username="Lira", email="lira@gmail.com", senha="123456")
#   usuario2 = Usuario (username="Joao", email="joao@gmail.com", senha="123456")
#   database. session. add(usuario)
#   database.session.add(usuario2)
#   database. session. commit()

# ---------------------------Buscar usuario---------------------------------------
  # meus_usuarios = Usuario.query.all()
  # print(meus_usuarios[0].posts)

# ---------------------------Buscar usuario com where---------------------------------------
#   meu_usuario = Usuario.query.filter_by(id=2).first()
#   print(meu_usuario.email)

# ---------------------------Criar um post---------------------------------------
  # meu_post = Post(id_usuario = 1, titulo = 'Primeiro Post do Lira', corpo = 'Lira Voando')
  # database.session.add(meu_post)
  # database.session.commit()

# ---------------------------Buscar usuario---------------------------------------
  # posts = Post.query.all()
  # print(posts[0].autor.email)

# ----------------------------Deletar BD--------------------------------
  # database.drop_all()