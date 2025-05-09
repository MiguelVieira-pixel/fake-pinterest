from FakePinterest import database, app
from FakePinterest.models import User, Post

with app.app_context():
    database.create_all()