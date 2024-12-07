import logging

from flask import Flask, redirect, url_for
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from .core import init_app as core_init
from .auth import init_app as auth_init
from .config import config_map


# Initializing extensions.
db = SQLAlchemy()
migrate = Migrate()


def create_app(config_name: str = 'default'):
    app = Flask(__name__)

    # Setting gunicorn logger as app logger.
    gunicorn_logger = logging.getLogger("gunicorn.error")
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)

    # Getting a Configuration Class or Using Default Config.
    config_class = config_map.get(config_name, config_map['default'])
    app.config.from_object(config_class)

    if app.config.get('SECRET_KEY') == 'default-secret-key':
        app.logger.warning('Insecure SECRET_KEY is being used! You need to set environment variable "SECRET_KEY".')

    # Initializing extensions.
    db.init_app(app)
    migrate.init_app(app, db)

    # Initializing BluePrints.
    core_init(app)
    auth_init(app)

    @app.errorhandler(404)
    def page_not_found(error):
        return redirect(url_for('core.index'))

    from .auth.models import User

    return app