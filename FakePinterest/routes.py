#criar as rotas do nosso site(links)
from flask import render_template, url_for
from FakePinterest import app
from flask_login import login_required

from FakePinterest.forms import FormLogin, FormCreateAccount

@app.route("/", methods=["GET", "POST"])
def homepage():
    formlogin = FormLogin()
    return render_template("index.html", form=formlogin)

@app.route("/createAccount", methods=["GET", "POST"])
def create_account():
    formcreateaccount = FormCreateAccount()
    return render_template("createAccount.html", form=formcreateaccount)

@app.route("/profile/<user>")
@login_required
def profile(user):
    return render_template("profile.html", user=user)
