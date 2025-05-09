from FakePinterest import database
from datetime import datetime



class User(database.Model):
    id = database.Collumn(database.Integer, primary_key=True)
    username = database.Collumn(database.String, nullable=False)
    email = database.Collumn(database.String, nullable=False, unique=True)
    senha = database.Collumn(database.String, nullable=False)
    post = database.Relationship("Post", backref="User", lazy=True)

class Post(database.Model):
    id = database.Collumn(database.Integer, primary_key=True)
    imagem = database.Collumn(database.String, default="default.png")
    data_criacao = database.Collumn(database.DateTime, nullable=False,     default=datetime.utcnow())
    id_usuario = database.Collumn(database.Integer, database.ForeignKey("user.id"), nullable=False)
