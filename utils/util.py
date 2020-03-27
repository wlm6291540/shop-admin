import hashlib


def make_password(password):
    encrypt = hashlib.md5()
    encrypt.update(password.encode('utf8'))
    return encrypt.hexdigest()
