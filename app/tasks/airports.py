from flask import current_app
from app import celery
from app.api.airport.service import AirportService

        
@celery.task(bind=True)
def create_airport_task(self, payload):
    return AirportService.create_airport(payload)

@celery.task(bind=True)
def update_airport_task(self, id, payload):
    return AirportService.update_airport(id, payload)

@celery.task(bind=True)
def delete_airport_task(self, id):
    return AirportService.delete_airport(id)