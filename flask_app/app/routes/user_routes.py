from flask import Blueprint

# Create a blueprint instance
user_bp = Blueprint('user', __name__)

@user_bp.route('/users')
def get_users():
    return {"message": "List of users"}