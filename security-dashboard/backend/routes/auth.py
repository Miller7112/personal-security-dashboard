from flask import Blueprint, request, jsonify

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/signup', methods=['POST'])
def signup():
    # Importing here to avoid circular import
    from backend.models.user import add_user
    
    data = request.get_json()

    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        return jsonify({"error": "All fields (username, email, password) are required!"}), 400

    # Check if the username is already taken
    from backend.models.user import users_db  
    if username in users_db:
        return jsonify({"error": "Username is taken! Choose a different one."}), 400

    add_user(username, email, password)  # Add the user with the hashed password

    return jsonify({"message": "Signup successful! You can now log in."}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    # Importing here to avoid circular import
    from backend.models.user import check_user_credentials
    
    data = request.get_json()

    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Username and password are required!"}), 400

    if check_user_credentials(username, password):
        return jsonify({"message": "Login successful!"}), 200
    return jsonify({"error": "Invalid credentials"}), 401
