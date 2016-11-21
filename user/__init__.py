from flask import Blueprint

user = Blueprint('users', __name__)

from . import views, forms
