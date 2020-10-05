# Model Schemas
from app import ma

from .airport import Airport


class AirportSchema(ma.Schema):
    class Meta:
        # Fields to expose, add more if needed.
        load_instance = True
        fields = (
            'id',
            'name',
            'city',
            'country',
            'iata',
            'icao',
            'latitude',
            'longitude',
            'altitude',
            'timezone',
            'dst',
            'tz',
            'type',
            'source',
        )
