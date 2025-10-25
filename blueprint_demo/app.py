from flask import Flask
from user import user_bp
from admin import admin_bp

app = Flask(__name__)

app.register_blueprint(user_bp, url_prefix="/user")

app.register_blueprint(admin_bp, url_prefix="/admin")

@app.route('/')
def home():
    return "This is the main app home page"

if __name__ == '__main__':
    app.run(debug=True)