from flask import Blueprint

bp = Blueprint('auth', __name__)

from .routes import *


def init_app(app):
    app.register_blueprint(bp, url_prefix='/auth')
