from flask import Blueprint

post = Blueprint('posts', __name__)

from  . import views
