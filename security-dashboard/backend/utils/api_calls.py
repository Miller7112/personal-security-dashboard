import hashlib
import requests

HIBP_API_URL = "https://api.pwnedpasswords.com/range/"

def check_pwned_password(password: str) -> int:
    """Checks if a password has been exposed in data breaches using Have I Been Pwned API."""
    sha1_hash = hashlib.sha1(password.encode()).hexdigest().upper()
    prefix, suffix = sha1_hash[:5], sha1_hash[5:]

    response = requests.get(f"{HIBP_API_URL}{prefix}")
    if response.status_code == 200:
        hashes = (line.split(':') for line in response.text.splitlines())
        for h, count in hashes:
            if h == suffix:
                return int(count)  # Number of times password appears in breaches
    return 0  # Not found in breaches
