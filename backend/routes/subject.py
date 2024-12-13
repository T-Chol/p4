from flask import Blueprint
from api.baseresource import BaseResource

subject_bp = Blueprint('subject', __name__)

@subject_bp.route('/subjects', methods=['GET'])
def handle_subjects():
    return 'List of subjects'  # Replace with actual logic

class SubjectResource(BaseResource):
    def get(self):
        return {'message': 'subjectt details'}  # Replace with actual data
