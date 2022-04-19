from database.db import User
from app import db
from services.pass_code import encrypt


class RegisterService:
    def __init__(self, email: str = False, user: str = False, password: str = False):
        self.email = email
        self.user = user
        self.password = password

    def register(self):
        user_validation = User.query.filter_by(name=self.user).first() or \
                          User.query.filter_by(email=self.user).first()

        if not user_validation:
            add_user = User(name=self.user, email=self.email, password=encrypt(self.password))
            db.session.add(add_user)
            db.session.commit()
            return True

        return False
