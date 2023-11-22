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

CORS(app, supports_credentials=True)  # Enable CORS for all routes

bycrpt = Bcrypt(app)

migrate = Migrate(app, db)





# login student
@app.route('/api/student/login', methods=['POST'])
def student_login():
    try:
        if request.method == 'POST':
            data = request.get_json()
            password = data.get('password')
            hash_pass = bycrpt.generate_password_hash(password)
            new_user = Student(matric_no=data.get('matric_no'), password=hash_pass)
            db.session.add(new_user)
            db.session.commit()
            # start a session
            session['stud_mat'] = data.get('matric_no')
            session['logged_in'] = True


            return jsonify({'message': 'User created successfully', data:new_user}),201
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# # Signup Student
# @app.route('/api/student/register', methods= ['POST'])



if __name__ == "__main__":
    app.run(debug=True)
