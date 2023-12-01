from flask_sqlalchemy import SQLAlchemy
from uuid import uuid4
from datetime import datetime

db = SQLAlchemy()



def get_uuid():
    return uuid4().hex


class Student(db.Model):
    __tablename__ = "students"
    id = db.Column(db.String(40), default=get_uuid, nullable=False)
    matric_no = db.Column(db.String(10), primary_key=True, unique=True, nullable=False)
    first_name = db.Column(db.String(32),nullable=False)
    last_name = db.Column(db.String(32), nullable=False)
    other_name = db.Column(db.String(32), nullable=False)
    faculty = db.Column(db.Enum('SOC', 'SOS'), nullable=False)
    department = db.Column(db.Enum('software engineering', 'information system'),nullable=False)
    image = db.Column(db.Text)
    password = db.Column(db.Text, nullable=False) 


    def __init__(self, matric_no, first_name, last_name,
                 other_name, faculty, department, image, password):
        self.matric_no = matric_no
        self.first_name = first_name
        self.last_name = last_name
        self.other_name = other_name
        self.faculty = faculty
        self.department = department
        self.image = image
        self.password = password


    def __repr__(self):
        return f"<User {self.matric_no}>"


    def save(self):
        db.session.add(self)
        db.session.commit()


class Course(db.Model):
     __tablename__ = "course"
     course_code = db.Column(db.String(32), primary_key=True ,nullable=False)
     course_title = db.Column(db.String(32))
     course_lecturer = db.Column(db.String(32))
     course_credit = db.Column(db.String(32), nullable=False)


class Result(db.Model):
    __tablename__ = 'results'
    id = db.Column(db.String(32), default = get_uuid, primary_key=True, nullable=False)
    course_code = db.Column(db.String(32), db.ForeignKey('course.course_code'), nullable=False)
    matric_no =db.Column(db.String(32), db.ForeignKey('students.matric_no'), nullable=False )
    mark =db.Column(db.Integer, nullable=False)
    grade_point = db.Column(db.Integer)
    session = db.Column(db.String(32), nullable=False)
    semester = db.Column(db.String(32), db.Enum('first', 'second'), nullable=False)


class Admin_Base(db.Model):
    __tablename__ = 'admin'
    id = db.Column(db.String(32), default = get_uuid, primary_key=True, nullable=False)
    first_name = db.Column(db.String(32), nullable=False)
    last_name = db.Column(db.String(32), nullable=False)
    email = db.Column(db.String(40), unique=True, nullable=False)
    phone_number = db.Column(db.String(32))
    password = db.Column(db.String(32), nullable=False)


    def __init__(self, first_name, last_name, email, phone_number, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.password = password


    def save(self):
        db.session.add(self)
        db.session.commit()
