from flask import render_template, request, redirect, url_for, flash, session
from flask_login import login_user, current_user
from api.twitter_oauth2 import Endpoint, TwitterOauth

from datetime import timedelta
from app import app

from services.login_service import LoginService
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
        if social_type == 'twitter':
            token = TwitterOauth(request.args).twitter_oauth()
            user = Endpoint(token)

            session['username'] = user.info_user()['data']['name']

            return redirect(url_for("route.social"))

        elif current_user.is_authenticated:
            return redirect(url_for("route.home"))

        elif "username" in session:
            return redirect(url_for("route.social"))

        return render_template("login.html")
