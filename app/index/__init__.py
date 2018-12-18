from flask import Blueprint
index_bp = Blueprint('index',__name__)

from . import models,routes,views