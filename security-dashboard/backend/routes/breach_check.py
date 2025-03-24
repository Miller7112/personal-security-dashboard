from flask import Blueprint, request, jsonify
from backend.utils.api_calls import check_pwned_password  # Function to check breach status

# Create the blueprint for breach check
breach_check_bp = Blueprint('breach_check', __name__)

@breach_check_bp.route('/check_breach', methods=['POST'])
def check_breach():
    # Get the password from the request body
    data = request.json
    password = data.get("password", "")

    if not password:
        return jsonify({"error": "No password provided"}), 400

    # Check the breach status
    breach_count = check_pwned_password(password)

    response = {
        "password": password,
        "breach_count": breach_count,
        "safe": breach_count == 0,
        "message": (
            "✅ Password is safe (not found in breaches)." if breach_count == 0
            else f"⚠️ Your password was found in {breach_count} breaches! Consider changing it immediately."
        )
    }

    return jsonify(response)
