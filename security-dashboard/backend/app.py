from flask import Flask
from backend.routes.auth import auth_bp
from backend.routes.password_check import password_check_bp
from backend.routes.breach_check import breach_check_bp  # Import the new breach check blueprint

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(auth_bp, url_prefix='/api/auth')  # Auth routes (signup, login)
app.register_blueprint(password_check_bp, url_prefix='/api/password')  # Password check routes
app.register_blueprint(breach_check_bp, url_prefix='/api/breach')  # Breach check routes

# Set up any necessary app configurations
app.config['SECRET_KEY'] = 'your_secret_key'

@app.route('/')
def home():
    return "Welcome to the Personal Security Dashboard!"

if __name__ == "__main__":
    # Run the app
    app.run(debug=True)
