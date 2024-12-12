from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app import db
from .validations import generate_reg_no
class Teacher(db.model):
    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    reg_no = Column(String, unique=True, default=lambda: generate_reg_no('T'))
    name = Column(String, nullable=False)
    subject = Column(String, nullable=False)
    
    students = relationship('Student', back_populates='teacher')
