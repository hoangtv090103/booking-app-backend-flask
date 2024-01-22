from flask import Flask, request, jsonify

from database import db_session, DATABASE_URL
from models import Account, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


@app.route('/')
def index():
    return "Hello World"


@app.route('/tutor-manager')
def tutor_manager():
    result = User.query.all()
    if not result:
        return jsonify({'message': 'No users found'})
    result = [{
        'id': user.id,
        'name': user.name,
        'email': user.email
    } for user in result]
    return jsonify(result)


@app.route('/tutor-manager/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login_acc = request.json.get('login')
        password = request.json.get('password')
        account = Account.query.filter_by(login=login_acc).first()
        if account and account.password == password:
            return jsonify(
                {
                    'login': account.login,
                    'username': account.user.name,
                    'email': account.user.email
                }
            )
        return jsonify({'message': 'Invalid login or password'})


if __name__ == "__main__":
    # user = User.query.filter_by(name='admin')
    # user.account_id = Account.query.filter_by(login="admin").first().id
    # db_session.commit()
    app.run(port=5000, debug=True)
