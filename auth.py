# coding: utf-8


class Auth:

    def __init__(self):
        self.accounts = {}

    def find(self, hashed_email):
        if hashed_email in self.accounts:
            return True
        else:
            return False

    def login(self, hashed_email, email):
        self.accounts[hashed_email] = email

    def logout(self, hashed_email):
        if hashed_email in self.accounts:
            del self.accounts[hashed_email]

    def get_email(self, hashed_email):
        if hashed_email in self.accounts:
            return self.accounts[hashed_email]
        else:
            return ''
