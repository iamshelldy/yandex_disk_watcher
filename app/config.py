import os
from datetime import timedelta


BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    """Base configuration."""
    SECRET_KEY = os.getenv('SECRET_KEY', 'default-secret-key')
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL',
                                        f'sqlite:///{BASE_DIR}/default.db')
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=30)
    REDIS_URL = os.getenv('REDIS_URL', 'redis://localhost:6379/0')


class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True


class TestingConfig(Config):
    """Testing configuration."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


# Dictionary for selecting a configuration.
config_map = {
    'default': Config,
    'development': DevelopmentConfig,
    'testing': TestingConfig,
}
