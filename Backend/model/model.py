from flask_sqlalchemy import SQLAlchemy
from uuid import uuid4
from datetime import datetime
from sqlalchemy import event


db = SQLAlchemy()



def get_uuid():
    return uuid4().hex


class Student(db.Model):
    __tablename__ = "students"
    id = db.Column(db.String(40),default=get_uuid)
    matric_no = db.Column(db.String(16), primary_key=True,unique=True, nullable=False) 
    first_name = db.Column(db.String(32),nullable=False)
    middle_name = db.Column(db.String(32))
    last_name = db.Column(db.String(32), nullable=False)
    faculty = db.Column(db.Enum('SOC', 'SOS'), nullable=False)
    department = db.Column(db.String(32),db.Enum('software engineering', 'information system',),nullable=False)
    level = db.Column(db.Enum('100','200','300','400','500'),nullable=False)
    image = db.Column(db.Text)
    password = db.Column(db.Text, nullable=False) 


    def __init__(self, matric_no, first_name, last_name,middle_name, faculty, department, image, password, level):
        self.matric_no = matric_no
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.faculty = faculty
        self.department = department
        self.level = level
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
     course_credit = db.Column(db.Integer, nullable=False)

     def __init__(self, course_code, course_title, course_lecturer, course_credit):
        self.course_code = course_code
        self.course_title = course_title
        self.course_lecturer = course_lecturer
        self.course_credit = course_credit


class Result(db.Model):
    __tablename__ = 'results'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    course_code = db.Column(db.String(32), db.ForeignKey('course.course_code'), nullable=False)
    matric_no = db.Column(db.String(32), db.ForeignKey('students.matric_no'), nullable=False)
    mark = db.Column(db.Integer, nullable=False)
    grade_point = db.Column(db.Integer)
    grade_unit = db.Column(db.Integer)
    total = db.Column(db.Integer)
    total_course_unit = db.Column(db.Integer)
    course_unit = db.Column(db.Integer, nullable=False)
    session = db.Column(db.String(32), nullable=False)
    semester = db.Column(db.Enum('first', 'second'), nullable=False)
    level = db.Column(db.Integer, nullable = True)
    
    __table_args__ = (
        db.UniqueConstraint('course_code'),
    )


    def __init__(self, course_code, matric_no, mark, course_unit, session, semester, level, grade_unit=None, grade_point=None):
        self.course_code = course_code
        self.matric_no = matric_no
        self.mark = mark
        self.course_unit = course_unit
        self.session = session
        self.grade_unit = self.calculate_grade_unit(mark) if grade_unit is None else grade_unit
        self.semester = semester
        self.grade_point = self.calculate_grade_point() if grade_point is None else grade_point
        self.level = int(level) if level is not None else None

        # Auto-fill other fields based on instructions
        self.total_course_unit = self.calculate_total_course_unit()
        self.total = self.calculate_total()

    def calculate_grade_unit(self, mark):
        if mark >= 70:
            return 5
        elif 60 <= mark < 70:
            return 4
        elif 50 <= mark < 60:
            return 3
        elif 45 <= mark <= 49:
            return 2
        else:
            return 0

    def calculate_grade_point(self):
        return self.grade_unit * self.course_unit

    def calculate_total_course_unit(self):
        # This should contain the addition of all the numbers in course unit
        # Implement this based on your specific requirement
        return self.course_unit

    def calculate_total(self):
        if self.total_course_unit != 0:
            return self.grade_point / self.total_course_unit
        else:
            return 0
# Event listener for generating a UUID before insert
@event.listens_for(Result, 'before_insert')
def before_insert(mapper, connection, target):
    target.id = get_uuid()

# Assuming get_uuid is a function that generates a UUID
def get_uuid():
    # Replace this with your UUID generation logic
    return 'generated_uuid'

@event.listens_for(Result, 'before_update')
def validate_units(mapper, connection, target):
    if target.grade_unit < 0 or target.total_course_unit < 0:
        raise ValueError('grade_unit and total_course_unit must be non-negative')


# Event listener for generating a UUID before insert
@event.listens_for(Result, 'before_insert')
def before_insert(mapper, connection, target):
    target.id = get_uuid()

# Assuming get_uuid is a function that generates a UUID
def get_uuid():
    # Replace this with your UUID generation logic
    return 'generated_uuid'

# Validate grade_unit and total_course_unit
# @validates('grade_unit', 'total_course_unit')
# def validate_units(key, value):
#     if value < 0:
#         raise ValueError(f'{key} must be non-negative')
#     return value
    


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
