from flask import Blueprint
from api.baseresource import BaseResource

teacher_bp = Blueprint('teacher', __name__)

@teacher_bp.route('/teachers', methods=['GET'])
def handle_teachers():
    return 'List of teachers'  # Replace with actual logic

class TeacherResource(BaseResource):
    def get(self):
        return {'message': 'Teachers details'}  # Replace with actual data
