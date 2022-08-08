from flask import session, redirect, url_for
from flask_login import logout_user


def logout_controller():
    logout_user()
    session.pop("username", None)
    return redirect(url_for("route.login"))
