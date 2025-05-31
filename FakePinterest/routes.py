#criar as rotas do nosso site(links)
from flask import render_template, url_for,redirect
from FakePinterest import app, database, bcrypt
from FakePinterest.models import User, Post
from flask_login import login_required, login_user, logout_user, current_user
from FakePinterest.forms import FormLogin, FormCreateAccount, FormPhotoPost
import os
from werkzeug.utils import secure_filename

@app.route("/", methods=["GET", "POST"])
def homepage():
    formLogin = FormLogin()
    if formLogin.validate_on_submit():
        user = User.query.filter_by(email=formLogin.email.data).first()
        if user and bcrypt.check_password_hash(user.password, formLogin.password.data):
            login_user(user, remember=True)
            return redirect(url_for("profile", id_usuario=user.id))

    return render_template("index.html", form=formLogin)

@app.route("/createAccount", methods=["GET", "POST"])
def create_account():
    formcreateaccount = FormCreateAccount()

    if formcreateaccount.validate_on_submit():
        print("Formulário válido")
        password = bcrypt.generate_password_hash(formcreateaccount.password.data)
        user = User(username=formcreateaccount.username.data, password=password, email=formcreateaccount.email.data)
        database.session.add(user)
        database.session.commit()
        login_user(user, remember=True)
        return redirect(url_for("profile", id_usuario=user.id))
    
    # Se o formulário não for válido, imprime os erros
    if formcreateaccount.errors:
        print("Erros de validação:", formcreateaccount.errors)
    return render_template("createAccount.html", form=formcreateaccount)

@app.route("/profile/<id_usuario>", methods=["GET", "POST"])
@login_required
def profile(id_usuario):
    if int(id_usuario) == int(current_user.id):
        form_photo = FormPhotoPost()
        if form_photo.validate_on_submit():
            file = form_photo.photo.data
            secure_name = secure_filename(file.filename)
            #Salva o arquivo na pasta 'static/phostos_posts'
            path = os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config["UPLOAD_FOLDER"], secure_name)
            file.save(path)
            #Registra o post no banco de dados
            photo = Post(imagem=secure_name, id_usuario=current_user.id)
            database.session.add(photo)
            database.session.commit()
        return render_template("profile.html", user=current_user, form=form_photo)
    else:
        user = User.query.get(int(id_usuario))
        return render_template("profile.html", user=user, form=None)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("homepage"))


