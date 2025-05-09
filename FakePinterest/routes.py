#criar as rotas do nosso site(links)
from flask import render_template, url_for
from FakePinterest import app
from flask_login import login_required
@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/profile/<user>")
@login_required
def profile(user):
    return render_template("profile.html", user=user)
