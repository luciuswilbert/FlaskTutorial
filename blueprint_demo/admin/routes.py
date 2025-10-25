from flask import Flask, Blueprint

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/hello', methods=['GET'])
def hello_admin():
    return "Hello, Admin!"