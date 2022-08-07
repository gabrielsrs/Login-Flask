from flask import render_template, request, redirect, url_for, flash, session
from services.login_service import LoginService
from flask_login import login_user
from database.db import User


def login_controller():
    if request.method == "POST":
        user = request.form.get("username")
        password = request.form.get("password")

        data_users = LoginService(user, password)

        if data_users.login():
            user_object = User.query.filter_by(name=user).first()
            login_user(user_object)
            # Use sessions for validate the access to home

            remember = request.form.get('remember') == "remember"

            if remember:
                session.permanent = True

            session.permanent = False

            session["username"] = data_users.get_user_name()

            return redirect(url_for("route.home"))

        else:
            # Error of Login
            flash("message_alert", "Seu usuário ou senha estão incorretos")
            return redirect(url_for("route.login"))

    else:
        if "username" in session:
            return redirect(url_for("route.home"))

        return render_template("login.html")


