import pymysql
import bcrypt


class Mysql:

    connection = pymysql.connect(host="localhost",
                                 user="root", password="",
                                 db="cadastro",
                                 charset="utf8mb4")

    def __init__(self, email="", user="", password=""):
        self.email = email
        self.user = user
        self.password = password

    def conf_login(self):
        """
        Confirm the information of login, verify if user exist in DB.
        :return: Exist(1) or not exist(0) for route
        """
        with self.connection.cursor() as cursor:
            user_res = cursor.execute(f"select email, user from login where email = '{self.email}' or "
                                      f"user = '{self.user}';")

            # When user login is wrong return None and the output is a error by bcrypt
            try:
                cursor.execute(f"select password from login where email = '{self.email}' or user = '{self.user}';")
                user_hash_password = cursor.fetchone()

                if bcrypt.checkpw(self.password, user_hash_password[0]):
                    login_password = cursor.execute(f"select password from login where email = '{self.email}' or "
                                                    f"user = '{self.user}' and password = '{user_hash_password[0]}';")

                else:
                    login_password = 0

            except:
                login_password = 0

        return True if user_res and login_password else False

    def register(self):
        """
        Register of user
        :return State of user registered
        """
        with self.connection.cursor() as cursor:
            res_check = cursor.execute(f"select email, user from login where email = '{self.email}' or "
                                       f"user = '{self.user}';")

            if not res_check:
                hash_password = bcrypt.hashpw(self.password, bcrypt.gensalt())
                cursor.execute(f"insert into login values(default, '{self.email}', '{self.user}','{hash_password}');")
                return True

            else:
                return False

    def get_user_name(self):
        with self.connection.cursor() as cursor:
            cursor.execute(f"select user from login where email = '{self.email}' or user = '{self.user}';")
            get_user_name = cursor.fetchone()
            return get_user_name
