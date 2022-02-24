from flask import request, redirect, flash, url_for, render_template
from services.register_service import RegisterService


def register_controller():

    if request.method == "POST":
        email = request.form.get("email")
        user = request.form.get("username")
        password = request.form.get("password")

        data_users = RegisterService(email, user, password)
        info_users = data_users.register()

        if info_users.register() is True:
            flash("message_alert", f"Usuário {user} cadastrado com sucesso")
            return redirect(url_for("route.login"))

        else:
            flash("message_alert", "Erro ao cadastrar usuário")
            return redirect(url_for("route.register_user"))

    return render_template("register.html")
