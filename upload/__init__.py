from flask import Blueprint

upload = Blueprint('uploads', __name__)

from . import views
