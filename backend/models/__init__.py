# from .teacher import Teacher
# from .student import Student
# from .subject import Subject


from flask import Flask
from flask_migrate import Migrate
from .database import db
from dotenv import load_dotevn
from flask_bcrypt import Bcrypt
def create_app():
    global bcrypt
    load_dotevn()
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_prefixed_env()

    bcrypt = Bcrypt(app)


    Migrate (app, db)
    db.init_app(app)

    @app.route("/")
    def home():
        return "hello world!"
    from api import bp

    return app