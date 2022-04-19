from database.db import User
from datetime import datetime
from services.pass_code import check_match


class LoginService:
    """
        Route of login and validations' users
        :return: Page of login


        create validation by search with the user is register in sqlalchemy
    """

    def __init__(self, user: str = False, password: str = False):
        self.user = user
        self.password = password

    def login(self):
        try:
            user_validation = User.query.filter_by(name=self.user).first() or \
                              User.query.filter_by(email=self.user).first()
            # False(have user) True(don't have user)

            if user_validation is not None:
                password_db = User.query.filter_by(name=self.user).first().password

                return True if check_match(self.password, password_db) else False

        except Exception as error:
            log(error, self.user)
            return False

    def get_user_name(self):
        get_user_name = User.query.filter_by(name=self.user).first() or \
                        User.query.filter_by(email=self.user).first()

        return get_user_name.name


def log(err, user):
    with open("database/log_db.txt", "a") as execute:
        execute.write(f"{datetime.now()}, {err}, {user} \n")
