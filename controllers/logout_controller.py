from flask import session, redirect, url_for


def logout_controller():
    session.pop("username", None)
    return redirect(url_for("route.login"))
