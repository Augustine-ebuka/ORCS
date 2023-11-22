from flask_sqlalchemy import SQLAlchemy
from uuid import uuid4
from datetime import datetime

db = SQLAlchemy()


def get_uuid():
    return uuid4().hex


class Student(db.Model):
    __tablename__ = "users"
    id = db.Column(db.String(32),default=get_uuid)
    matric_no = db.Column(db.String(10), primary_key=True,unique=True)
    first_name = db.Column(db.String(32))
    last_name = db.Column(db.String(32))
    other_name = db.Column(db.String(32))
    faculty = db.Column(db.Enum('SOC', 'SOS'))
    department = db.Column(db.Enum('software engineering', 'information system'))
    image = db.Column(db.Text)
    password = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<User {self.matric_no}>"

# class Link(db.Model):
#     __tablename__ = "userlinks"
#     id = db.Column(db.String(32), primary_key=True, unique=True, default=get_uuid)
#     short_url = db.Column(db.String(255), unique=False, default=None)
#     long_url = db.Column(db.String(255), unique=False)
#     user_id = db.Column(db.String(255), db.ForeignKey('users.id'))
#     clicks = db.Column(db.Integer, unique=False, default=0)
#     slug = db.Column(db.String(255), unique=False, default=None)
#     active = db.Column(db.Boolean, unique=False, default=True)
#     title = db.Column(db.String(255), unique=False, default=None)
#     created_at = db.Column(db.DateTime, default=func.now())