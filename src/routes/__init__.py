from flask import render_template, redirect, url_for, Blueprint, flash, session
from flask_login import current_user

from controllers.login_controller import login_controller
from controllers.logout_controller import logout_controller
from controllers.register_controller import register_controller

import error

handle = Blueprint("route", __name__)


@handle.route("/", methods=["POST", "GET"])
@handle.route("/login", methods=["POST", "GET"])
@handle.route("/login/<social_type>", methods=["POST", "GET"])
def login(social_type=None):
    """
        Route of login and validations' users
        :return: Page of login
    """
    return login_controller(social_type)


@handle.route("/home")
def home():
    if current_user.is_authenticated:
        return render_template("home.html")

    return redirect(url_for("route.login"))


@handle.route("/social")
def social():
    if "username" in session:
        flash("message_home", session["username"])

        return render_template("social.html")
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
