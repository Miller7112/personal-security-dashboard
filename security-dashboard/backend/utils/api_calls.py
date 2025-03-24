from backend.models.breach import BreachHistory  
import hashlib
import requests

HIBP_API_URL = "https://api.pwnedpasswords.com/range/"

def check_pwned_password(password: str) -> int:
    """Checks if a password has been exposed in data breaches using Have I Been Pwned API."""
    sha1_hash = hashlib.sha1(password.encode()).hexdigest().upper()
    prefix, suffix = sha1_hash[:5], sha1_hash[5:]

    # Check if the password is already in the database
    existing_breach = BreachHistory.get_breach_by_hash(sha1_hash)
    if existing_breach:
        return existing_breach.breach_count  # Return the stored breach count if available

    # Send request to HIBP API for the range (first 5 characters of SHA-1)
    response = requests.get(f"{HIBP_API_URL}{prefix}")
    
    if response.status_code == 200:
        hashes = (line.split(':') for line in response.text.splitlines())
        
        # Check if the suffix matches any of the hashes
        for h, count in hashes:
            if h == suffix:
                breach_count = int(count)
                # Store the breach history in the database
                BreachHistory.create_breach(sha1_hash, breach_count)
                return breach_count

    # If no match is found, store the breach as 0
    BreachHistory.create_breach(sha1_hash, 0)
    return 0
