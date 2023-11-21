from flask import Flask, url_for, request, redirect
from markupsafe import escape

app = Flask(__name__)


@app.route('/<name>')
def home(name):
    return f"hello {escape(name)}"

@app.route('/user/', methods=['GET'])
def show_user_profile():
    # show the user profile for that user
    name = request.args.get('name')
    return f'{name}'

@app.route("/me/")
def me_api():
    
    return {
        "username": "name",
        "theme": "name",
        "image": "image",
    }
with app.test_request_context():
    print(url_for('show_user_profile', name='John'))    
if(__name__ == "__main__"):
    app.run(debug=True)  