"""
Extensions module

Each extension is initialized when app is created.
"""

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from celery import Celery


db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()

def make_celery(app):
    celery = Celery(
        __name__,
        broker=app.config['CELERY_BROKER']
        # backend=app.config['CELERY_BACKEND'],
    )
    return celery
