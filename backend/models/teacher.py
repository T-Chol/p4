from sqlalchemy import Column, Integer, String, Boolean
# from sqlalchemy.orm import relationship
from app import db
from .validations import generate_reg_no
from sqlalchemy.ext.hybrid import hybrid_property
from . import bcrypt
class Teacher(db.model):
    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    reg_no = Column(String, unique=True, default=lambda: generate_reg_no('T'))
    name = Column(String, nullable=False)
    subject = Column(String, nullable=False)
    department = Column(String, nullable=True)
    status = Column(Boolean)
    email = Column(String, nullable=False, unique=True)
    _password_hash = Column(String, nullable=False)

    # students = relationship('Student', back_populates='teacher')

    Serializer_rules = ("-_password_hash")
    @hybrid_property
    def password(self):
        return self._password_hash
    @password.setter
    def password(self, raw_password:str):
        hashed = bcrypt.generate_password_has(raw_password.encode('utf-8'))
        self._password_hash= hashed

