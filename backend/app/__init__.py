from flask import Flask
from models import db

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
    db.init_app(app)

    from routes import home_bp
    app.register_blueprint(home_bp, url_prefix='/')
    
    with app.app_context():
        db.create_all()
    return app