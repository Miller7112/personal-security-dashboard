# backend/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize the database object
db = SQLAlchemy()

def create_app():
    # Initialize the Flask app
    app = Flask(__name__)

    # Set configuration for the app
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'  # Change to your actual database URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable modification tracking to save resources
    app.config['SECRET_KEY'] = 'your_secret_key'  # Use a strong, secret key in production

    # Initialize the db with the Flask app
    db.init_app(app)

    # Register blueprints for routing
    from backend.routes.auth import auth_bp
    from backend.routes.password_check import password_check_bp
    from backend.routes.breach_check import breach_check_bp

    # Register routes with the app
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(password_check_bp, url_prefix='/api/password')
    app.register_blueprint(breach_check_bp, url_prefix='/api/breach')

    return app
