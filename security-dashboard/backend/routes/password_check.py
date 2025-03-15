import hashlib
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

def check_password_breach(password):
    sha1_password = hashlib.sha1(password.encode()).hexdigest().upper()
    prefix, suffix = sha1_password[:5], sha1_password[5:]
    
    hibp_url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(hibp_url)
    
    if response.status_code == 200:
        breaches = {line.split(':')[0]: int(line.split(':')[1]) for line in response.text.splitlines()}
        return breaches.get(suffix, 0)  # Return number of times password was found
    
    return -1  # API request failed

@app.route('/check_password', methods=['POST'])
def check_password():
    data = request.json
    password = data.get("password", "")
    
    if not password:
        return jsonify({"error": "No password provided"}), 400
    
    breach_count = check_password_breach(password)
    response = {
        "password": password,
        "breach_count": breach_count,
        "safe": breach_count == 0,
        "message": "Password is safe" if breach_count == 0 else f"Password found in {breach_count} breaches! Consider changing it."
    }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
