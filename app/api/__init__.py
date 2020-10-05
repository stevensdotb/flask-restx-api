from flask_restx import Api
from flask import Blueprint

from .airport.controller import api as airport_ns

# Import controller APIs as namespaces.
api_bp = Blueprint("api", __name__)

api = Api(api_bp, title="API", description="Main routes.")

# API namespaces
api.add_namespace(airport_ns)
