from flask import redirect, url_for


def error():
    return redirect(url_for("login.html"))
