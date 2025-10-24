from flask import Flask
from app.routes.user_routes import user_bp  # Import blueprint

def create_app():
    app = Flask(__name__)
    
    # Register blueprint
    app.register_blueprint(user_bp, url_prefix='/api')
    
    return app