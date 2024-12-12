from sqlalchemy import Date ,Column, ForeignKey, Integer, String, Boolean, TIMESTAMP
from sqlalchemy.orm import relationship
from app import db
class Student(db.model):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    reg_no = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    subject = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    enrolment_date = Column(TIMESTAMP)
    dob = Column(Date, nullable=True)
    status = Column(Boolean)


    teacher_id = Column(Integer, ForeignKey('teachers.reg_no'))  # Relationship with Teacher

    # teacher = relationship('Teacher', back_populates='students')
