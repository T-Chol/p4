# api/__main__.py
from flask import Flask
from routes import blueprints  # Import your blueprints
from api import bp as api_bp  # Import API blueprint

app = Flask(__name__)

# Register all blueprints
for blueprint in blueprints:
    app.register_blueprint(blueprint)

# Register API blueprint
app.register_blueprint(api_bp)

if __name__ == "__main__":
    app.run(debug=True)

