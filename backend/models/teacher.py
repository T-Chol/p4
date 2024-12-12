from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app import db
from .validations import generate_reg_no
class Teacher(db.model):
    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    reg_no = Column(String, unique=True, default=lambda: generate_reg_no('T'))
    name = Column(String, nullable=False)
    subject = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    department = Column(String, nullable=True)
    status = Column(Boolean)

    # students = relationship('Student', back_populates='teacher')
