#criar os formularios do site
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from FakePinterest.models import User

class FormLogin(FlaskForm):
    imail = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")

class FormCreateCount(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    username = StringField("Username", validators=[DataRequired()])
    passoword = PasswordField("Passoword", validators=[DataRequired(), Length(6,20), EqualTo("Confirm")])
    confirm = PasswordField("Confirm", validators=[DataRequired(), EqualTo("Passoword")])
    submit = SubmitField("Create Account")

def validate_email(self, email):
    user = User.query.filter_by(email=email.data).first()
    if user:
        return ValidationError("Email already registered")
    