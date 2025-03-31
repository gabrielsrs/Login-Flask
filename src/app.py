from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta
from flask_login import LoginManager
import os

app = Flask(__name__, instance_relative_config=True)

login_manager = LoginManager()
login_manager.init_app(app)

app.config.from_object("config.Config")

db = SQLAlchemy(app)

app.permanent_session_lifetime = timedelta(
    days=int(app.config["DAYS"])
)
