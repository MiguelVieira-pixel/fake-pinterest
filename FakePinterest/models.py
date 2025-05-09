from FakePinterest import database
from datetime import datetime



class User(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False, unique=True)
    senha = database.Column(database.String, nullable=False)
    post = database.Relationship("Post", backref="User", lazy=True)

class Post(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    imagem = database.Column(database.String, default="default.png")
    data_criacao = database.Column(database.DateTime, nullable=False,     default=datetime.utcnow())
    id_usuario = database.Column(database.Integer, database.ForeignKey("user.id"), nullable=False)
