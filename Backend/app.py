from flask import Flask, jsonify, request, session, abort
from flask_migrate import Migrate
from model.model import Student, db, Course, Result, Admin_Base
from flask_cors import CORS, cross_origin
from flask_bcrypt import Bcrypt
from flask_login import (LoginManager, login_user,
                         logout_user, login_required,
                         current_user)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://dev_test:DevLog#1@localhost/orcs_db'
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

            student = Student.query.filter_by(matric_no = data.get('matric_no') ).first()
            
            if not student:
                 return({"message": "student not found"}), 401
            
            if not bycrpt.check_password_hash(student.password, password):
                return jsonify({"message":"UnAuthenticated"}), 401

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
                return jsonify({"error": "student already exist"})
            if data:
                hash_pass = bycrpt.generate_password_hash(data.get('password'))
                new_stu = Student(
                    matric_no=data.get('matric_no'),
                    first_name = data.get('first_name'),
                    last_name = data.get('last_name'),
                    other_name = data.get('other_name'),
                    faculty = data.get('faculty'),
                    department = data.get('department'),
                    image = data.get('image'),
                    password = hash_pass
                    )      
                new_stu.save()
                session['stud_mat'] = data.get('matric_no')
                return jsonify({'message': 'student created successfully!'}), 201
            else:
                return jsonify({"message":"missing field"}), 400
            
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/student/info', methods=['GET'])
def student_info():
    try:
        if request.method == 'GET':
            # matric_no = session.get('stud_mat')
            matric_no = '79146'
            
            student_data = db.session.query(Student, Result).filter(
                    Student.matric_no == Result.matric_no).filter(Student.matric_no == matric_no).all()
            # student = db.session.query(Student).filter_by(Student.matric_no = matric_no).first()
            if student_data:
                student_list = []
                student, result = student_data[0]
                student_info = {
                    'Student Info': '',
                    'matric_no': student.matric_no,
                    'first_name': student.first_name,
                    'last_name': student.last_name,
                    'other_name': student.other_name,
                    'faculty': student.faculty,
                    'department': student.department,
                    'Result': {
                        'course_code': result.course_code,
                        'session': result.session,
                        'semester': result.semester,
                        'mark': result.mark,
                        'grade_point': result.grade_point
                    }
                }
            student_list.append(student_info)
            return jsonify(student_list), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


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
            
            if not check_if_exist:
                hash_pass = bycrpt.generate_password_hash(password)
                # Save signup to admin Database
                new_admin = Admin_Base(
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
                 return({"message": "admin account with this email not found"}), 401
            
            if not bycrpt.check_password_hash(admin.password, password):
                return abort(401)

            # This section needs revision.
            session['admin_email'] = data.get('email')
            session['is_logged_in'] = True
            return jsonify({'message': 'User logged in successfully'}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/student/result/upload', methods=['POST'])
def upload_student_result():
    try:
        if request.method == 'POST':
            # Get Post Request
            # This is indended to get the student info from the frontend i.e Admin Panel
            data = request.get_json()
            course_code = data.get('course_code')
            matric_no = data.get('matric_no')
            mark = data.get('mark')
            grade_point = data.get('grade_point')
            session = data.get('session')
            semester = data.get('semester')

            # Insert a function that computes the grade point based on marks

            # Update Student Result Marks and Grade Point for the semester and session
            # More Notes: This section is simple as making sure that it filter the selected student
            # based on the matric number, semester and session and update the marks and grade point
            update_result = db.session.query(Result).filter(
                    matric_no=matric_no, semester=semester, session=session).first()
            if update_result:
                update_result.mark = mark
                update_result.grade_point = grade_point
                db.session.commit()
                return jsonify({"message": "Result updated successfully"}), 200
            else:
                return jsonify({"message": "Result with this matric number not found"}), 404
 
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Any thing below here is for testing
@app.route('/api/test')
def test_api():
    try:
        import json
        from model.test import (get_student,
                                intert_data_to_student,
                                insert_data_to_result,
                                insert_data_to_course)
    
        data = intert_data_to_student()
        course = insert_data_to_course()
        result = insert_data_to_result()
            
        data.save()
        # db.session.add(data)
        db.session.add(course)
        db.session.add(result)
        db.session.commit()
        
        student = get_student("12345")
        return f"'Student Data': {student}"

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/more/test', methods=['GET'])
def more_test():
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
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


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
