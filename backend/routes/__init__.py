#routes/__init__.py
from .home import home_bp
from .student import student_bp, StudentResource  # Import student routes
from .subject import subject_bp, SubjectResource
from .teacher import teacher_bp,TeacherResource

blueprints = [
    home_bp,
    student_bp,  # Register student blueprint
    subject_bp,
    teacher_bp
]

route_resource =[
    StudentResource,
    SubjectResource,
    TeacherResource
]