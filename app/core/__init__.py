from flask import Blueprint

bp = Blueprint('core', __name__)

from .routes import *


def init_app(app):
    app.register_blueprint(bp)
