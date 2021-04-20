from flask import Blueprint

web = Blueprint('web', __name__, url_prefix='/')

from app.web import main
from app.web import post_table
from app.web import get_table
from app.web import pic