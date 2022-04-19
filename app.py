from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta


app = Flask(__name__)

app.config.from_object("config.Config")
app.secret_key = app.config["SECRET_KEY"]

app.config["SQLALCHEMY_DATABASE_URI"] = app.config["SQLALCHEMY_DB"]
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

app.permanent_session_lifetime = timedelta(
    days=int(app.config["DAYS"])
)
