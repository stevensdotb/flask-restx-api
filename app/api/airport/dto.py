from flask_restx import Namespace, fields


class AirportDTO:

    api = Namespace("airports", description="Airports CRUD Operations")
    aiport = api.model(
        "Airport Model",
        {
            'id': fields.Integer,
            'name': fields.String,
            'city': fields.String,
            'country': fields.String,
            'iata': fields.String,
            'icao': fields.String,
            'latitude': fields.Float,
            'longitude': fields.Float,
            'altitude': fields.Float,
            'timezone': fields.Float,
            'dst': fields.String,
            'tz': fields.String,
            'type': fields.String,
            'source': fields.String,
            'updated_at': fields.DateTime
        },
    )

    data_resp = api.model(
        "Airport Response",
        {
            "message": fields.String,
            "status": fields.Boolean,
            "data": fields.Nested(aiport),
        },
    )

    data_file_upload_resp = api.model(
        'Airport File Data Response',
        {
            "status": fields.Boolean,
            "message": fields.String
        }
    )