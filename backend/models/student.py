from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app import db
class Student(db.model):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    reg_no = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    subject = Column(String, nullable=False)
    mark = Column(Integer, nullable=False)


    teacher_id = Column(Integer, ForeignKey('teachers.id'))  # Relationship with Teacher

    teacher = relationship('Teacher', back_populates='students')
