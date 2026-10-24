import string

from Training.pass_utils import generate_password

def test_generate_password_returns_string():
    password = generate_password()
    assert isinstance(password, str)

def test_generate_password_length():
    password = generate_password()
    assert 12 <= len(password) <= 20

def test_generate_password_uses_valid_characters():
    password = generate_password()
    alphabet = string.ascii_letters + string.digits + string.punctuation
    assert all(char in alphabet for char in password)

def test_generate_password_generates_random_values():
    passwords = {generate_password() for _ in range(10)}
    assert len(passwords) > 1