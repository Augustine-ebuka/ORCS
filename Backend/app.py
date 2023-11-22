from flask import Flask, jsonify, request, session
from flask_migrate import Migrate
from model.model import Student,db
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/orcs_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.secret_key = 'your_secret_key'  # Set your secret key for sessions

CORS(app, supports_credentials=True)  # Enable CORS for all routes


migrate = Migrate(app, db)


@app.route('/api/users', methods=['POST'])
def create_user():
    try:
        if request.method == 'POST':
            data = request.get_json()
            new_user = Student(matric_no=data.get('matric_no'), password=data.get('password'))

            db.session.add(new_user)
            db.session.commit()

            return jsonify({'message': 'User created successfully'}),201
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
