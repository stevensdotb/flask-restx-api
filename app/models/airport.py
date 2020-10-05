from datetime import datetime
from app import db


# Alias common DB names
Column = db.Column
Model = db.Model


class Airport(Model):
    """ User model for storing airports related data """
    __tablename__ = 'airports'

    id = Column(db.Integer, primary_key=True)
    name = Column(db.String(150), index=True)
    city = Column(db.String(50))
    country = Column(db.String(20))
    iata = Column(db.String(10))
    icao = Column(db.String(10))
    latitude = Column(db.Float)
    longitude = Column(db.Float)
    altitude = Column(db.Float)
    timezone = Column(db.Float)
    dst = Column(db.String(10))
    tz = Column(db.String(50))
    type = Column(db.String(20), default="airport")
    source = Column(db.String(20))
    created_at = Column(db.Date, default=datetime.now())
    updated_at = Column(db.DateTime, onupdate=datetime.now())
    deleted = Column(db.Boolean, default=False)

    def __init__(self, **kwargs):
        super(Airport, self).__init__(**kwargs)

    def __repr__(self):
        return f"<Airport {self.name}({self.id})>"
