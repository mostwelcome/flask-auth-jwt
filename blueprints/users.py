from functools import wraps

import jwt

from flask import Blueprint, request, jsonify

from database.models.tables.user import User
from managers.users import register_user,get_all_users,user_login

USERS_BLUEPRINT = Blueprint('user', __name__)


# decorator for verifying jwt
def jwt_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify(
                {'message': 'Token is missing!'}
            ), 401
        try:
            # decoding token
            data = jwt.decode(token, 'your secret key')
            current_user = User.query \
                .filter_by(public_id=data['public_id']) \
                .first()
        except jwt.DecodeError:
            return jsonify(
                {
                    'message': 'Token is invalid!'
                }
            ), 401
        return f(current_user, *args, **kwargs)

    return wrapper


@USERS_BLUEPRINT.route('/')
@jwt_required
def get_all_user(current_user):
    return get_all_users()


@USERS_BLUEPRINT.route('/login', methods=['POST'])
# @jwt_required
def login():
    auth = request.get_json()
    print(auth)
    return user_login(auth)


@USERS_BLUEPRINT.route('/register', methods=['POST'])
def register():
    pass
    # creates a dictionary of the form data
    data = request.get_json()
    print(data)
    return register_user(data)
