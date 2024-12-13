# api/__init__.py
from flask import Blueprint
from flask_restful import Api
from .baseresource import BaseResource, home  # Import concrete resources
# Import models (ensure models are defined or replace with placeholders)
from routes import blueprints, route_resource
bp = Blueprint("api_routes", __name__, url_prefix="/api")
api = Api(bp)

# Define routes
for resource in route_resource:
    if resource:
        api.add_resource(resource, f"/{resource.__name__.lower()}")
# api.add_resource(route_resource.teacherResource, "/teachers")

for blueprint in blueprints:
    bp.register_blueprint(blueprint)
    # api.add_resource(blueprint, f"/{blueprint.name}")
# Register resources
# for endpoint, model in routes:
#     resource = model if model else BaseResource
#     api.add_resource(
#         resource,
#         f"/{endpoint}"
#     )
