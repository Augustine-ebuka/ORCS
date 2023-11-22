from flask_sqlalchemy import SQLAlchemy
from uuid import uuid4
from datetime import datetime
from sqlalchemy import func

db = SQLAlchemy()

def get_uuid():
    return uuid4().hex

# current_datetime = datetime.now()
# formatted_datetime = current_datetime.strftime("%b %d, %Y, %I:%M %p")
# current_time = datetime.now().time()
# formatted_time = current_time.strftime("%I:%M %p")
# data_obj= datetime.now()



class Student(db.Model):
    __tablename__ = "users"
    id = db.Column(db.String(32), unique=True, default=get_uuid)
    matric_no = db.Column(db.String(10), unique=True, primary_key=True)
    password = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<User {self.email}"


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