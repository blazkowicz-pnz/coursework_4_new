import base64
import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    SECRET_KEY = "secret"
    JSON_AS_ASCII = False
    ITEMS_PER_PAGE = 12
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    TOKEN_EXPIRE_MINUTES = 15
    TOKEN_EXPIRE_DAYS = 130
    JWT_ALGO = "HS256"
    HASH_NAME = "sha256"
    HASH_SALT = "salt"
    HASH_ITERATIONS = 100_000


class TestingConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(
        os.path.dirname(BASEDIR), "project.db"
    )
