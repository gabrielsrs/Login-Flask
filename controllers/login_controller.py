from flask import render_template, request, redirect, url_for, flash, session
from flask_login import login_user, current_user

from datetime import timedelta
from app import app

from services.login_service import LoginService
from services.oauth2_options import Options
from database.db import User


def login_controller(social_type):
    if request.method == "POST":
        user = request.form.get("username")
        password = request.form.get("password")

        data_users = LoginService(user, password)

        if data_users.login():
            user_object = User.query.filter_by(name=user).first()
            remember = request.form.get('remember') == "remember"

            login_user(user=user_object,
                       remember=remember,
                       duration=timedelta(days=int(app.config["DAYS"]))
                       )

            return redirect(url_for("route.home"))

        else:
            flash("message_alert", "Seu usuário ou senha estão incorretos")
            return redirect(url_for("route.login"))

    else:
        if social_type:
            third_party = Options(social_type=social_type, code=request.args)
            result = third_party.social()

            session['username'] = result

            return redirect(url_for("route.social"))

        elif current_user.is_authenticated:
            return redirect(url_for("route.home"))

        elif "username" in session:
            return redirect(url_for("route.social"))

        return render_template("login.html")
