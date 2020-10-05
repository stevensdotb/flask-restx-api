from flask import current_app

from app.utils import err_resp, message, internal_err_resp
from app.models import Airport
from app.extensions import db
from .utils import serialize_file_data

class AirportService:
    @staticmethod
    def get_airport_data(id):
        """ Get airport data by id """
        if not (airport := Airport.query.filter_by(id=id).first()):
            return err_resp("Airport not found!", "airport_404", 404)

        from .utils import load_data

        try:
            airport_data = load_data(airport)

            resp = message(True, f"'{airport.name}' airport data")
            resp["data"] = airport_data
            return resp, 200

        except Exception as error:
            current_app.logger.error(error)
            return internal_err_resp()

    @staticmethod
    def create_airport(data):
        """ Create a new airport registry """

        from .utils import load_data

        try:
            airport = Airport(**data)
            db.session.add(airport)
            db.session.commit()

            resp = message(True, f"New airport saved.")
            resp["data"] = load_data(airport);
            
            return resp, 200

        except Exception as error:
            current_app.logger.error(error)
            return internal_err_resp()
 

    @staticmethod
    def delete_airport(id):
        """Detele a specific airport by id"""
        if not (airport := Airport.query.filter_by(id=id).first()):
            return err_resp("Airport not found!", "airport_404", 404)

        from .utils import load_data

        try:
            airport.deleted = True # logic deletion
            db.session.commit()

            airport_data = load_data(airport)

            resp = message(True, f"'{airport.name}' airport deleted")
            resp["data"] = airport_data
            
            return resp, 200

        except Exception as error:
            current_app.logger.error(error)
            return internal_err_resp()

    @staticmethod
    def update_airport(id, data):
        """Update a specific airport by id"""
        
        if not (airport := Airport.query.filter_by(id=id).first()):
            return err_resp("Airport not found!", "airport_404", 404)

        from .utils import load_data

        try:
            for key in data.keys():
                if data.get(key, False): # Existing key in airport object
                    setattr(airport, key, data[key])

            db.session.commit()

            airport_data = load_data(airport)

            resp = message(True, f"'{airport.name}' airport updated")
            resp["data"] = airport_data

            return resp, 200

        except Exception as error:
            current_app.logger.error(error)
            return internal_err_resp()
    
    @staticmethod
    def upload_data_from_csv(file):
        """ Receives data to upload to airport table """
        
        try:
            file_data = serialize_file_data(file)
            # Add airports registry
            for single_airport in file_data:
                airport = Airport(**single_airport)
                db.session.add(airport)
            
            db.session.commit()
            resp = message(True, "Airports data uploaded with success")

            return resp, 200

        except Exception as error:
                    current_app.logger.error(error)
                    return internal_err_resp()



class AirportAsyncService:
    """ Asyncrous CRUD operations """

    @staticmethod
    def create_airport(data):
        """ Create a new airport registry """

        from .utils import load_data

        try:
            airport = Airport(**data)
            db.session.add(airport)
            db.session.commit()

            resp = message(True, f"Your request to create a new ")
            resp["data"] = load_data(airport);
            
            return resp, 200

        except Exception as error:
            current_app.logger.error(error)
            return internal_err_resp()
 

    @staticmethod
    def delete_airport(id):
        """Detele a specific airport by id"""
        if not (airport := Airport.query.filter_by(id=id).first()):
            return err_resp("Airport not found!", "airport_404", 404)

        from .utils import load_data

        try:
            airport.deleted = True # logic deletion
            db.session.commit()

            airport_data = load_data(airport)

            resp = message(True, f"'{airport.name}' airport deleted")
            resp["data"] = airport_data
            
            return resp, 200

        except Exception as error:
            current_app.logger.error(error)
            return internal_err_resp()

    @staticmethod
    def update_airport(id, data):
        """Update a specific airport by id"""
        
        if not (airport := Airport.query.filter_by(id=id).first()):
            return err_resp("Airport not found!", "airport_404", 404)

        from .utils import load_data

        try:
            for key in data.keys():
                if data.get(key, False): # Existing key in airport object
                    setattr(airport, key, data[key])

            db.session.commit()

            airport_data = load_data(airport)

            resp = message(True, f"'{airport.name}' airport updated")
            resp["data"] = airport_data

            return resp, 200

        except Exception as error:
            current_app.logger.error(error)
            return internal_err_resp()
    
    @staticmethod
    def upload_data_from_csv(file):
        """ Receives data to upload to airport table """
        
        try:
            file_data = serialize_file_data(file)
            # Add airports registry
            for single_airport in file_data:
                airport = Airport(**single_airport)
                db.session.add(airport)
            
            db.session.commit()
            resp = message(True, "Airports data uploaded with success")

            return resp, 200

        except Exception as error:
                    current_app.logger.error(error)
                    return internal_err_resp()
