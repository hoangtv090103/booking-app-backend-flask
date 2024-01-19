from flask import Flask, jsonify, request
from models import User, Account
from database import db_session

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:f5GBG1F4C46-24eABgAAE2GAE*D4ECaf@' \
                                        'viaduct.proxy.rlwy.net:34049/railway'


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
    request_data = request.get_json()
    username = request_data['username']
    password = request_data['password']
    result = Account.query.filter_by(login=username, password=password).first()
    if result:
        return jsonify(
            {
                'login': result.login,
                # 'username': result.user.name,
                # 'email': result.user.email
            }
        )
    else:
        return jsonify(
            {
                'message': 'Invalid username or password'
            }
        )


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == '__main__':
    from models import User
    from database import init_db
    init_db()
    acc = Account(login='admin', password='admin')
    db_session.add(acc)
    db_session.commit()
    app.run(port=5000, debug=True)
