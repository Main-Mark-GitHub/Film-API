from hashlib import sha256


def make_password(string):
    return sha256(string.encode()).hexdigest()