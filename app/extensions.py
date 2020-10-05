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

# def make_celery(app):
#     celery = Celery(
#         app.import_name,
#         backend=app.config['CELERY_BACKEND'],
#         broker=app.config['CELERY_BROKER']
#     )
#     celery.conf.update(app.config)

#     class ContextTask(celery.Task):
#         def __call__(self, *args, **kwargs):
#             with app.app_context():
#                 return self.run(*args, **kwargs)

#     celery.Task = ContextTask
#     return celery
