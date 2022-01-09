import hashlib
class User:

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = hashlib.sha256(password.encode()).digest()

