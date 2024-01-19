from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello World"


@app.route('/tutor-manager')
def tutor_manager():
    return {
        'name': 'Flask API',
        'dob': '1999-01-01',
        'email': '123@gmail.com'
    }


if __name__ == '__main__':
    app.run(port=5000, debug=True)
