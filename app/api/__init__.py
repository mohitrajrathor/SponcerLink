__version__ = '1'
__author__ = 'Mohit Raj Rathor'

from flask import Blueprint


api = Blueprint('api', __name__, url_prefix=f'/api/v{__version__}')

