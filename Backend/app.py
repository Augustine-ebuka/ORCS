from flask import Flask, jsonify, request, session
from flask_migrate import Migrate
from model.model import Student,db
from flask_cors import CORS, cross_origin
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/orcs_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.secret_key = 'your_secret_key'  # Set your secret key for sessions
# initialize the app with the extension
db.init_app(app)
CORS(app, supports_credentials=True)  # Enable CORS for all routes

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

            student = Student.query.filter_by(matric_no = data.get(matric_no) ).first()
            
            if student is None:
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
                db.session.add(new_stu)
                db.session.commit()
                session['stud_mat'] = data.get('matric_no')
                return jsonify({'message': 'student created successfully!'}), 201
            else:
                return jsonify({"message":"missing field"}), 400
            
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
                    



if __name__ == "__main__":
    app.run(debug=True)
