from flask import Blueprint

bp = Blueprint('insert', __name__, url_prefix='/insert')

from insert import routes

