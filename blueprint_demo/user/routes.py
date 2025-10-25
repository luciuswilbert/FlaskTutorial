from flask import Flask, jsonify, Blueprint

user_bp = Blueprint('user', __name__)

@user_bp.route('/hello', methods=['GET'])
def hello_user():
    return "Hello, User!"