import random
import string

def create_random_login(length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def create_random_password(length=10):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

def create_random_firstname(length=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length)).capitalize()
