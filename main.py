from flask import Flask, render_template, request, redirect, url_for, flash, session
from database import Mysql
from datetime import timedelta

app = Flask(__name__)
app.secret_key = b"secret_key"
app.permanent_session_lifetime = timedelta(days=30)


@app.route("/login", methods=["POST", "GET"])
def login():
    """
    Route of login and validations' users
    :return: Page of login
    """
    if request.method == "POST":
        user = request.form.get("username")
        password = request.form.get("password")

        info_users = Mysql(email=user, user=user, password=password)

        if info_users.conf_login():
            # Use sessions for validate the access to home
            if request.form.get('remember') == "remember":
                session.permanent = True

            session["username"] = info_users.get_user_name()[0]

            return redirect(url_for("home"))

        else:
            # Error of Login
            flash("message_alert", "Seu usuário ou senha estão incorretos")
            return redirect(url_for("login"))
    else:
        if "username" in session:
            return redirect(url_for("home"))

        return render_template("login.html")


@app.route("/home")
def home():
    if "username" in session:
        flash("message_home", session["username"])
        return render_template("home.html")

    return redirect(url_for("login.html"))


@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("login"))


@app.route("/error")
def error():
    """
    :return: Page error
    """
    return redirect(url_for("login.html"))


@app.route("/register", methods=["POST", "GET"])
def register_user():
    """
    :return:Page register user
    """
    if request.method == "POST":

        email = request.form.get("email")
        user = request.form.get("username")
        password = request.form.get("password")

        info_users = Mysql(email=email, user=user, password=password)

        if info_users.register() is True:
            flash("message_alert", f"Usuário {user} cadastrado com sucesso")
            return redirect(url_for("login"))

        else:
            flash("message_alert", "Erro ao cadastrar usuário")
            return redirect(url_for("register_user"))
    return render_template("register.html")


if __name__ == '__main__':
    app.run(debug=True)
