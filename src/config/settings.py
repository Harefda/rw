from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    TRACK_MODIFICATIONS: bool

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'

SETTINGS = Settings()


class Config(object):
    """Base config."""
    SECRET_KEY = None
    SESSION_COOKIE_NAME = None
    SQLALCHEMY_DATABASE_URI = SETTINGS.DATABASE_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = SETTINGS.TRACK_MODIFICATIONS


class ProdConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False
    DATABASE_URI = SETTINGS.DATABASE_URL


class DevConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
    DATABASE_URI = SETTINGS.DATABASE_URL