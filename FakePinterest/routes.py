#criar as rotas do nosso site(links)
from flask import render_template, url_for,redirect
from FakePinterest import app, database, bcrypt
from FakePinterest.models import User, Post
from flask_login import login_required, login_user, logout_user
from FakePinterest.forms import FormLogin, FormCreateAccount

@app.route("/", methods=["GET", "POST"])
def homepage():
    formlogin = FormLogin()
    return render_template("index.html", form=formlogin)

@app.route("/createAccount", methods=["GET", "POST"])
def create_account():
    formcreateaccount = FormCreateAccount()
    if formcreateaccount.validate_on_submit():
        password = bcrypt.generate_password_hash(formcreateaccount.password.data)
        user = User(username=formcreateaccount.username.data, password=password, email=formcreateaccount.email.data)
        database.session.add(user)
        database.session.commit()
        login_user(user, remember=True)
        return redirect(url_for("profile", user=user.username))
    return render_template("createAccount.html", form=formcreateaccount)

@app.route("/profile/<user>")
@login_required
def profile(user):
    return render_template("profile.html", user=user)
