# api/baseresource.py
from flask_restful import Resource
from flask import request, jsonify

class BaseResource(Resource):
    def handle_error(self, error):
        """Handles errors and returns a standardized error response."""
        return jsonify({"error": str(error)}), 500

    def get_user_from_token(self):
        """Example: Parses the authorization token and retrieves the user."""
        token = request.headers.get("Authorization")
        if not token:
            return None, "Authorization token is missing"
        # Dummy logic for token validation; replace with actual logic
        if token == "valid-token":
            return {"id": 1, "name": "John Doe"}, None
        return None, "Invalid token"

    def validate_payload(self, payload, required_keys):
        """Validates that required keys are present in the payload."""
        missing_keys = [key for key in required_keys if key not in payload]
        if missing_keys:
            return False, f"Missing keys: {', '.join(missing_keys)}"
        return True, None




class home(BaseResource):
    def get(self):
        try:
            # Example: Use token-based authentication
            user, error = self.get_user_from_token()
            if error:
                return {"error": error}, 401

            return {"message": f"Hello {user['name']}!"}, 200
        except Exception as e:
            return self.handle_error(e)


# class StudentResource(BaseResource):
#     def get(self):
#         try:
#             students = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
#             return {"students": students}, 200
#         except Exception as e:
#             return self.handle_error(e)

# class SubjectResource(BaseResource):
#     def get(self):
#         try:
#             subjects = [{"id": 1, "name": "Math"}, {"id": 2, "name": "Science"}]
#             return {"subjects": subjects}, 200
#         except Exception as e:
#             return self.handle_error(e)
