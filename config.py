import os
from datetime import timedelta
from flask import current_app

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:

    CELERY_BROKER_URL = "amqp://myuser:mypassword@rabbitmq/"
    CELERY_RESULT_BACKEND = "rpc://"
    # Local without using Docker
    # CELERY_BROKER_URL = "amqp://myuser:mypassword@localhost/testvhost"



    # Change the secret key in production run.
    SECRET_KEY = os.environ.get("SECRET_KEY", os.urandom(24))
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = os.environ.get(
    #     "DATABASE_URL", ""  
    # )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Add logger


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    # In-memory SQLite for testing
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False
    # This app won't run on a prod environment. Ignore.
    # SQLALCHEMY_DATABASE_URI = os.environ.get( 
    #     "DATABASE_URL", "sqlite:///" + os.path.join(basedir, "data.sqlite")
    # )
    SQLALCHEMY_TRACK_MODIFICATIONS = False


config_by_name = dict(
    development=DevelopmentConfig,
    testing=TestingConfig,
    production=ProductionConfig,
    default=DevelopmentConfig,
)
