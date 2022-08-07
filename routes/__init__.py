from flask import render_template, redirect, url_for, flash, session, Blueprint, request

from controllers.login_controller import login_controller
from controllers.logout_controller import logout_controller
from controllers.register_controller import register_controller

import error

handle = Blueprint("route", __name__)


@handle.route("/", methods=["POST", "GET"])
@handle.route("/login", methods=["POST", "GET"])
def login():
    """
        Route of login and validations' users
        :return: Page of login
    """
    return login_controller()


@handle.route("/home")
def home():
    if "username" in session:
        flash("message_home", session["username"])

        return render_template("home.html")
    return redirect(url_for("route.login"))


@handle.route("/logout")
def logout():

    return logout_controller()


@handle.route("/error")
def error():
    """
    :return: Page error
    """
    return error()


@handle.route("/register", methods=["POST", "GET"])
def register_user():
    """
    :return:Page register user
    """
    return register_controller()
