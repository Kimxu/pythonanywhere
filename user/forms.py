from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from models import User


class LoginForm(Form):
    email = StringField('电子邮箱', validators=[Required(), Length(1, 64),
                                            Email()],id='email')
    password = PasswordField('密码', validators=[Required()],id='password')
    remember_me = BooleanField('记住密码',id='remember_me')
    submit = SubmitField('登录', id='submit')
