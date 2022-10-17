from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Email, Length
class SignupForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired(), Length(max=64)])
    lastname = StringField('Apellido', validators=[DataRequired(), Length(max=128)])
    password = PasswordField('Password', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Registrar')

class UserForm(FlaskForm):
    title = StringField('Tìtulo', validators=[])
    name = StringField('Nombre', validators=[DataRequired(), Length(max=128)])
    lastname = StringField('Apellido', validators=[DataRequired(), Length(max=128)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Enviar')