from flask import Flask, jsonify, request, session, abort
from flask_migrate import Migrate
from model.model import Student, db, Course, Result, Admin_Base
from flask_cors import CORS, cross_origin
from flask_bcrypt import Bcrypt
from flask_login import (LoginManager, login_user,
                         logout_user, login_required,
                         current_user)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/orcs_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.secret_key = 'your_secret_key'  # Set your secret key for sessions
# initialize the app with the extension
db.init_app(app)
CORS(app, supports_credentials=True)  # Enable CORS for all routes

login_manager = LoginManager()
login_manager.init_app(app)

bycrpt = Bcrypt(app)
with app.app_context():
    db.create_all()

migrate = Migrate(app, db)





# login student
@app.route('/api/student/login', methods=['POST'])
def student_login():
    try:
        if request.method == 'POST':
            data = request.get_json()
            
            password = data.get('password')
            matric_no = data.get('matric_no')
            if not password or not matric_no:
                return({"message": "password or matric no cannot be empty"}), 401

            student = Student.query.filter_by(matric_no = data.get('matric_no')).first()
            
            if not student:
                 return({"error": "student not found"}), 404
            
            if not bycrpt.check_password_hash(student.password, password):
                return jsonify({"error":"password incorrect"}), 401

            session['stud_mat'] = data.get('matric_no')
            session['is_logged_in'] = True
            return jsonify({'message': 'User logged in successfully'}), 200

        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# # Signup Student
@app.route('/api/student/register', methods= ['POST'])
def student_register():
    try:
        if request.method == 'POST':
            data = request.get_json()
            check_if_exist = Student.query.filter_by(matric_no = data.get('matric_no')).first()
            if check_if_exist:
                return jsonify({"error": "student already exist"}),403
            if data:
                hash_pass = bycrpt.generate_password_hash(data.get('password'))
                new_stu = Student(
                    matric_no=data.get('matric_no'),
                    first_name = data.get('first_name'),
                    middle_name = data.get('middle_name'),
                    last_name = data.get('last_name'),
                    faculty = data.get('faculty'),
                    department = data.get('department'),
                    level = data.get('level'),
                    image = data.get('image'),
                    password = hash_pass
                    )      
                db.session.add(new_stu)
                db.session.commit()
                session['stud_mat'] = data.get('matric_no')
                return jsonify({'message': 'student created successfully!'}), 201
            else:
                return jsonify({"error":"missing field"}), 400
            
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# fetch student info
@app.route('/api/student/info', methods=['GET'])
def student_info():
    try:
        if request.method == 'GET':
            matric_no = session.get('stud_mat')
            # matric_no = '73322'
            # student_data = db.session.query(Student, Result).filter(
            #         Student.matric_no == Result.matric_no).filter(Student.matric_no == matric_no).all()
            student_data = db.session.query(Student).filter_by(matric_no = matric_no).first()
            if student_data:
                student_list = []
                student = student_data
                student_info = {
                    'matric_no': student.matric_no,
                    'first_name': student.first_name,
                    'middle_name': student.middle_name,
                    'last_name': student.last_name,
                    'faculty': student.faculty,
                    'department': student.department,
                    'level': student.level,
                    'image': student.image
                }
                student_list.append(student_info)
            return jsonify({"message":student_list}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# admin signup
@app.route('/api/admin/signup', methods=['POST'])
def admin_signup():
    try:
        if request.method == 'POST':
            data = request.get_json()
            
            email = data.get('email')
            password = data.get('password')
            first_name = data.get('first_name')
            last_name = data.get('last_name')
            phone_number = data.get('phone_number')

            if not email or not password or not first_name or not last_name or not phone_number:
                return({"message": "all fields are required"}), 401

            check_if_exist = Admin_Base.query.filter_by(email=email).first()
            if check_if_exist:
                return jsonify({"error": "admin with this email already exist"})
            if data:
                hash_pass = bycrpt.generate_password_hash(password)
                # Save signup to admin Database
                new_admin=Admin_Base(
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    phone_number=phone_number,
                    password=hash_pass
                    )
                new_admin.save()
                return jsonify({'message': 'admin created successfully!'}), 201
            else:
                return jsonify({"message":"unable to create this admin account"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# admin loin
@app.route('/api/admin/login', methods=['POST'])
def admin_login():
    try:
        if request.method == 'POST':
            data = request.get_json()
            password = data.get('password')
            email = data.get('email')
            if not password or not email:
                return abort(401)

            admin = Admin_Base.query.filter_by(email = data.get('email')).first()
            
            if not admin:
                 return({"message": "admin account not found"}), 401
            
            if not bycrpt.check_password_hash(admin.password, password):
                return abort(401)

            session['admin_email'] = data.get('email')
            session['is_logged_in'] = True
            return jsonify({'message': 'User logged in successfully'}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/student/result/upload', methods=['POST', 'GET'])
def upload_student_result():
    try:
        # session['is_logged_in'] = True
        # session['stud_mat'] = matric_no
        if request.method == 'GET':
            matric_no = '73322'
            form_data = db.session.query(Student, Result).filter(
                    Student.matric_no == Result.matric_no).filter(Student.matric_no == matric_no).all()
            if form_data:
                student_info = []
                student, result = form_data[0]
                student_name = student.first_name
                student_lname = student.last_name
                student_othername = student.other_name
                student_name = student_name + ' ' + student_lname + ' ' + student_othername
                student_mark = result.mark
                student_grade = result.grade_point
                student_course = result.course_code
                student_session = result.session
                student_semester = result.semester
                student_info.append(student_name)
                student_info.append(student_mark) 
                student_info.append(student_grade)
                student_info.append(student_course)
                student_info.append(student_session)
                student_info.append(student_semester)
                return jsonify(student_info), 200

        if request.method == 'POST':
            # Get Post Request
            data = request.get_json()
            course_code = data.get('course_code')
            matric_no = data.get('matric_no')
            mark = data.get('mark')
            grade_point = data.get('grade_point')
            session = data.get('session')
            semester = data.get('semester')

            # Insert a function that computes the grade point based on marks

            data = request.get_json()
            matric_no = data.get('matric_no')
            
            # Filter Student Information Based on Matric No
            form_data = db.session.query(Student).filter(Student.matric_no == matric_no).all()
            if form_data:
                student_info = []
                student = form_data[0]
                student_info.append(student.first_name)
                student_info.append(student.last_name)
                student_info.append(student.other_name)
                student_info.append(student.faculty)
                student_info.append(student.department)
                return jsonify(student_info), 200
            else:
                return jsonify({'message': 'Student not found'}), 404

            # Filter Result based on Matric No
            form_data = db.session.query(Result).filter(Result.matric_no == matric_no).all()
            if form_data:
                result_info = []
                for result in form_data:
                    result_info.append({
                        'course_code': result.course_code,
                        'mark': result.mark,
                        'grade_point': result.grade_point,
                        'session': result.session,
                        'semester': result.semester
                    })
                return jsonify(result_info), 200
            else:
                return jsonify({'message': 'Result not found'}), 404

            upload_result = Result(
                course_code=course_code,
                matric_no=matric_no,
                mark=mark,
                grade_point=grade_point,
                session=session,
                semester=semester
            )
            db.session.add(upload_result)
            db.session.commit()

            # course_code = data.get('course_code')
            student_result = db.session.query(Student, Result).join(Result).filter(
                    Student.matric_no == Result.matric_no).all()

            return jsonify({'message': 'File uploaded successfully'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500


# @app.route('/api/test')
# def test_api():
#     try:
#         import json
#         from model.test import (get_student,
#                                 intert_data_to_student,
#                                 insert_data_to_result,
#                                 insert_data_to_course)
    
#         data = intert_data_to_student()
#         course = insert_data_to_course()
#         result = insert_data_to_result()
            
#         data.save()
#         # db.session.add(data)
#         db.session.add(course)
#         db.session.add(result)
#         db.session.commit()
        
#         student = get_student("12345")
#         return f"'Student Data': {student}"

#     except Exception as e:
#         return jsonify({'error': str(e)}), 500


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorised(error) -> str:
    """ Unautorized handler
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """ Forbidden Handler
    """
    return jsonify({"error": "Forbidden"}), 403


@app.errorhandler(405)
def method_not_allowed(error) -> str:
    """ Method Not Allowed Handler
    """
    return jsonify({"error": "Method not allowed - you are not authorized"}), 405


if __name__ == "__main__":
    app.run(debug=True)
