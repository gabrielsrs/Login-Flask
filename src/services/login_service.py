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
            # query return None if don't find a user

            if user_validation:
                return True if check_match(self.password, user_validation.password) else False

            else:
                log("User/E-mail not found", self.user)

        except Exception as error:
            log(error, self.user)
            return False


def log(err, user):
    with open("instance/database/db.log", "a") as execute:
        execute.write(f"{datetime.now()}, {err}, {user} \n")
