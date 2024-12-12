from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .validations import generate_reg_no

from app import db

class Subject(db.model):
    __tablename__ = "subjects"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    reg_no = Column(String, unique=True, default=lambda: generate_reg_no('UN-'))
    name = Column(String, nullable=False)
