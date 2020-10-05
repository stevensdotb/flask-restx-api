import os
from pprint import pprint

from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename
from flask import request, current_app
from flask_restx import Resource

from .service import AirportService
from .dto import AirportDTO
from app.tasks.airports import create_airport_task, delete_airport_task, update_airport_task

api = AirportDTO.api


@api.route("/upload")
class AirportsUpload(Resource):
    @api.doc(
        "Upload a new dataset from a CSV file",
        response={
            200: ("Data from file has been upload with success", AirportDTO.data_file_upload_resp),
            400: "The file data could not be upload it"
        }
    )
    def post(self):
        """ Upload an aiports dataset from a CSV file to the database """
        parse = api.parser()
        parse.add_argument('file', location='files', type=FileStorage, required=True)
        args = parse.parse_args()

        if (file := args["file"]) != '':

            filename = secure_filename(file.filename)
            file_path = os.path.join(current_app.config['UPLOAD_DATA_DIR'], filename)
            file.save(file_path)

            return AirportService.upload_data_from_csv(file_path)
        
        return "The file data could not be uploaded it", 400


@api.route("/<int:id>")
class Airport(Resource):
    @api.doc(
        "Get a specific airport",
        responses={
            200: ("Airport data successfully sent", AirportDTO.data_resp),
            404: "Aiport not found!"
        },
    )
    def get(self, id):
        """ Get a specific airport's data by their id """
        return AirportService.get_airport_data(id)
    
    @api.doc(
        "Update a specific airport",
        responses={
            200: ("Airport data successfully updated", AirportDTO.data_resp),
            404: "Aiport not found"
        },
    )
    def put(self, id):
        """ Update a specific airport's data by their id """
        return AirportService.update_airport(id, request.get_json())
    
    @api.doc(
        "Delete a specific airport",
        responses={
            200: ("Airport successfully deleted", AirportDTO.data_resp),
            404: "Airport not found"
        },
    )
    def delete(self, id):
        """ Delete a specific airport by their id """
        return AirportService.delete_airport(id)

@api.route("/")
class AirportCreate(Resource):

    @api.doc(
        "Create a new airport",
        responses={
            200: ("Airport successfully created", AirportDTO.data_resp),
            403: "Airport could not be created"
        },
    )
    def post(self):
        """ Create a new airport registry """
        return AirportService.create_airport(request.get_json())

"""
Routes for Aiports (create/update/delete) asyncronous operations
"""
@api.route("/<int:id>/async")
class AirportAsync(Resource):
    @api.doc(
        "Update a specific airport",
        responses={
            200: ("Airport data successfully updated", AirportDTO.data_resp),
            404: "Aiport not found"
        },
    )
    def put(self, id):
        """ Update a specific airport's data by their id """
        update_airport_task.delay(id, request.get_json())
        return f"Your request to update the airport has been sent.", 200
    
    @api.doc(
        "Delete a specific airport",
        responses={
            200: ("Airport successfully deleted", AirportDTO.data_resp),
            404: "Airport not found"
        },
    )
    def delete(self, id):
        """ Delete a specific airport by their id """
        delete_airport_task.delay(id)
        return f"Your request to delete the airport has been sent.", 200


@api.route("/async")
class AirportAsyncCreate(Resource):
    """ Create a new airport registry """

    @api.doc(
        "Create a new airport",
        responses={
            200: ("Airport successfully created", AirportDTO.data_resp),
            403: "Airport could not be created"
        },
    )
    def post(self):
        """ Get a specific airport's data by their id """
        create_airport_task.delay(request.get_json())
        return "Your request to create a new airport has been sent.", 200
