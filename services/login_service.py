from database.db import Mysql


class LoginService:
    """
        Route of login and validations' users
        :return: Page of login
    """

    def __init__(self, user: str = False, password: str = False):
        self.user = user
        self.password = password

    def login(self):

        info_users = Mysql(email=self.user, user=self.user, password=self.password)

        return info_users
