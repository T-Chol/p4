# routes/home.py
from flask import Blueprint
home_bp = Blueprint('home', __name__)
@home_bp.route('/', methods=['GET'])
def handle_home():
    return 'Hello World!'