# Import necessary utilities (security functions)
from backend.utils.security import hash_password, verify_password

# Simulating a simple database using a dictionary for demonstration purposes
users_db = {}

def add_user(username, email, password):
    """
    Add a new user to the 'database' (simulated).
    """
    hashed_password = hash_password(password)  # Hash the password before storing it
    users_db[username] = {
        "email": email,
        "password": hashed_password
    }

def check_user_credentials(username, password):
    """
    Check user credentials (verify password).
    """
    user = users_db.get(username)
    if user:
        return verify_password(user["password"], password)
    return False
