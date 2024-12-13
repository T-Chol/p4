# from app import db    
# from flask import Blueprint, request, jsonify
# from models import Subject
# students_bp = Blueprint('students_bp', __name__)

# @students_bp.route('/', methods=['POST'], strict_slashes=False)
# def add_students():
#     data = request.get_json()
#     if not all(key in data for key in ['name', 'subjects', 'episode_id']):
#         return jsonify({"error": "Missing required fields"}), 400
#     is_valid, error_message = validate_rating(data['rating'])
#     if not is_valid:
#         return jsonify({"error": error_message}), 400
#     episode_data = data.get('episode', {})
#     guest_data = data.get('guest', {})

#     episode = Episode.query.get(episode_data.get('id')) or Episode(
#         id=episode_data.get('id'),
#         date=episode_data.get('date'),
#         number=episode_data.get('number')
#     )
#     guest = Guest.query.get(guest_data.get('id')) or Guest(
#         id=guest_data.get('id'),
#         name=guest_data.get('name'),
#         occupation=guest_data.get('occupation')
#     )
#     appearance = Appearance(
#         rating=data['rating'],
#         guest_id=data['guest_id'],
#         episode_id=data['episode_id'],
#         episode=episode,
#         guest=guest
#     )

#     try:
#         db.session.add(appearance)
#         db.session.commit()
#         return jsonify({
#             "id": appearance.id,
#             "rating": appearance.rating,
#             "guest_id": appearance.guest_id,
#             "episode_id": appearance.episode_id,
#             "episode": {
#                 "date": episode.date,
#                 "id": episode.id,
#                 "number": episode.number
#             },
#             "guest": {
#                 "id": guest.id,
#                 "name": guest.name,
#                 "occupation": guest.occupation
#             }
#         }), 201
#     except Exception as e:
#         db.session.rollback()
#         return jsonify({"error": f"Database error: {str(e)}"}), 500
from flask import Blueprint
from api.baseresource import BaseResource

student_bp = Blueprint('student', __name__)

@student_bp.route('/students', methods=['GET'])

def handle_students():
    return 'List of students'  # Replace with actual logic

class StudentResource(BaseResource):
    def get(self):
        return {'message': 'Student details'}  # Replace with actual data
