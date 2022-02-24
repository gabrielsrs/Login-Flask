from flask import render_template, request, redirect, url_for, flash, session
from services.login_service import LoginService
from flask_login import (
    UserMixin,
    login_user,
    
)

def login_controller():
    if request.method == "POST":
        user = request.form.get("username")
        password = request.form.get("password")

        data_users = LoginService(user, password)
        info_users = data_users.login()

        if info_users.conf_login():
            # Use sessions for validate the access to home
            if request.form.get('remember') == "remember":
                session.permanent = True
            else:
                session.permanent = False

            session["username"] = info_users.get_user_name()[0]

            return redirect(url_for("route.home"))

        else:
            # Error of Login
            flash("message_alert", "Seu usuário ou senha estão incorretos")
            return redirect(url_for("route.login"))

    else:
        if "username" in session:
            return redirect(url_for("route.home"))

        return render_template("login.html")


