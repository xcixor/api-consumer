"""Api v1 blueprint."""
from flask import Blueprint

from flask_restful import Api

v_1 = Blueprint('v1', __name__, url_prefix='/api/v1')

API = Api(v_1)

from app.api_v1 import routes