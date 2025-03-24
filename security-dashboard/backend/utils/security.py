from pyzxcvbn import zxcvbn  # Import for password strength analysis

def check_password_strength(password):
    """
    Analyze password strength using zxcvbn.
    Returns a score (0-4) and feedback suggestions.
    """
    try:
        strength_result = zxcvbn(password)
        return strength_result['score'], strength_result['feedback']['suggestions']
    except Exception as e:
        # Handle any potential errors (e.g., empty passwords)
        return 0, [str(e)]
