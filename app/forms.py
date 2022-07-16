import wtforms as wf
from flask_wtf import FlaskForm
from wtforms import validators

from app.models import Customer, User



class CustomerForm(FlaskForm):
    name = wf.StringField(label="Имя", validators=[
        validators.DataRequired(),
    ])
    phone_number = wf.StringField(label="Номер телефона", validators=[
        validators.DataRequired(),
    ])
    item = wf.StringField(label="Вещи", validators=[
        validators.DataRequired(),
    ])
    quantity = wf.IntegerField(label="Вещи", validators=[
        validators.DataRequired(),
    ])
    price = wf.IntegerField(label="Вещи", validators=[
        validators.DataRequired(),
    ])
    submit = wf.SubmitField(label="Добавить")





class UserForm(FlaskForm):
    username = wf.StringField(label="Имя пользывателя", validators=[
        validators.DataRequired(),
        validators.Length(min=3, max=64)
        ])
    password = wf.PasswordField(label="Пароль",  validators=[
        validators.DataRequired(),
        validators.Length(min=3, max=64)
        ])
    submit = wf.SubmitField(label="Подтвердить")