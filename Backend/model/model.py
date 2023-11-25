from flask_sqlalchemy import SQLAlchemy
from uuid import uuid4
from datetime import datetime

db = SQLAlchemy()



def get_uuid():
    return uuid4().hex


class Student(db.Model):
    __tablename__ = "students"
    id = db.Column(db.String(32),default=get_uuid)
    matric_no = db.Column(db.String(10), primary_key=True,unique=True, nullable=False) 
    first_name = db.Column(db.String(32),nullable=False)
    last_name = db.Column(db.String(32), nullable=False)
    other_name = db.Column(db.String(32), nullable=False)
    faculty = db.Column(db.Enum('SOC', 'SOS'), nullable=False)
    department = db.Column(db.Enum('software engineering', 'information system'),nullable=False)
    image = db.Column(db.Text)
    password = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<User {self.matric_no}>"

class Course(db.Model):
     __tablename__ = "course"
     course_code = db.Column(db.String(32),primary_key = True ,nullable=False)
     course_title = db.Column(db.String(32))
     course_lecturer = db.Column(db.String(32))
     course_credit = db.Column(db.String(32), nullable = False)


class Result(db.Model):
    __tablename__ = 'results'
    id = db.Column(db.String(32), default = get_uuid, primary_key = True, nullable = False)
    course_code = db.Column(db.String(32), db.ForeignKey('course.course_code'), nullable = False)
    matric_no =db.Column(db.String(32),db.ForeignKey('students.matric_no'), nullable = False )
    mark =db.Column(db.Integer, nullable = False)
    grade_point = db.Column(db.Integer)
    session = db.Column(db.String(32), nullable = False)
    semester = db.Column(db.String(32),db.Enum('first', 'second') ,nullable = False)

