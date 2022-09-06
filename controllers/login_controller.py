from flask import render_template, request, redirect, url_for, flash, session
from flask_login import login_user, current_user
from api.twitter_oauth2 import TwitterEndpoint, TwitterOauth
from api.twitch_oauth2 import TwitchLogin, TwitchEndpoint

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
            user = TwitterEndpoint(token).info_user()

            session['username'] = user['data']['name']

            return redirect(url_for("route.social"))

        elif social_type == 'twitch':
            token = TwitchLogin(request.args).token()
            user = TwitchEndpoint(token).user_name()

            session['username'] = user['data'][0]['display_name']

            return redirect(url_for("route.social"))

        elif current_user.is_authenticated:
            return redirect(url_for("route.home"))

        elif "username" in session:
            return redirect(url_for("route.social"))

        return render_template("login.html")
