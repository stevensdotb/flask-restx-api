""" Top level module

This module:

- Contains create_app()
- Registers extensions
"""
from celery import Celery
from flask import Flask, current_app

# Import extensions
from .extensions import db, migrate, ma, make_celery
from config import Config

# Import config
from config import config_by_name


celery = Celery(__name__, 
    broker=Config.CELERY_BROKER_URL,
    # backend=Config.CELERY_RESULT_BACKEND
)

# celery = make_celery(current_app)


def create_app(config_name):    
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_by_name[config_name])
    app.config.from_pyfile('config.py')

    register_extensions(app)

    # Register blueprint
    from .api import api_bp

    app.register_blueprint(api_bp, url_prefix="/api")

    return app


def register_extensions(app):
    # Registers flask extensions
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)
    celery.conf.update(app.config)
    

