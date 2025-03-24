from flask import Blueprint, request, jsonify
from backend.utils.api_calls import check_pwned_password  # Function to check breach status
from backend.utils.security import check_password_strength  # Function to check strength

# Creating the blueprint
password_check_bp = Blueprint('password_check', __name__)

@password_check_bp.route('/check_password', methods=['POST'])
def check_password():
    data = request.json
    password = data.get("password", "")

    if not password:
        return jsonify({"error": "No password provided"}), 400

    # Check breach status
    breach_count = check_pwned_password(password)

    # Check strength
    strength_score, feedback = check_password_strength(password)

    response = {
        "password": password,
        "breach_count": breach_count,
        "safe": breach_count == 0,
        "strength_score": strength_score,
        "feedback": feedback,
        "message": (
            "✅ Password is strong and not found in breaches." if breach_count == 0 and strength_score >= 3
            else f"⚠️ Password is weak or found in {breach_count} breaches! Consider changing it."
        )
    }

    return jsonify(response)
