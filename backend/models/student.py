from sqlalchemy import Date ,Column, ForeignKey, Integer, String, Boolean, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy_serializer import SerializerMixin
from .database import db
from sqlalchemy.ext.hybrid import hybrid_method, hybrid_property
from . import bcrypt

class Student(db.model, SerializerMixin):
    __tablename__ = "students"
    role = Column(String, nullable= False, default="Student")
    id = Column(Integer,  nullable=False, autoincrement=True)
    reg_no = Column(Integer, unique=True, nullable=False)
    name = Column(String, nullable=False)
    subject = Column(String, nullable=False)
    enrolment_date = Column(TIMESTAMP)
    dob = Column(Date, nullable=True)
    status = Column(Boolean)
    email = Column(String, nullable=False, unique=True)
    _password_hash = Column(String, nullable=False)


    teacher_id = Column(Integer, ForeignKey('teachers.reg_no'))  # Relationship with Teacher

    # teacher = relationship('Teacher', back_populates='students')
    Serializer_rules = ("-_password_hash")
    @hybrid_property
    def password(self):
        return self._password_hash
    @password.setter
    def password(self, raw_password:str):
        hashed = bcrypt.generate_password_has(raw_password.encode('utf-8'))
        self._password_hash= hashed


def authenticate(self, raw_password:str):
    hashed = bcrypt.generate_password_has(raw_password.encode('utf-8'))
    return self._password == hashed