from database.db import Mysql


class RegisterService:
    def __init__(self, email: str = False, user: str = False, password: str = False):
        self.email = email
        self.user = user
        self.password = password

    def register(self):
        info_users = Mysql(email=self.email, user=self.user, password=self.password)

        return info_users
