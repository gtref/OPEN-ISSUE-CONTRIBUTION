import secrets
import string

def generate_password()-> str:
    """Generate a random password with a random length between 12 and 20 characters."""
    length = secrets.randbelow(20 - 12 + 1) + 12 
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password