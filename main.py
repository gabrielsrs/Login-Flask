from flask import Flask
from datetime import timedelta

app = Flask(__name__)

app.config.from_object("config.Config")

app.secret_key = bytes(app.config["SECRET_KEY"], encoding="ascii")
app.permanent_session_lifetime = timedelta(days=int(app.config["DAYS"]))


with app.app_context():
    from routes import handle

    app.register_blueprint(handle)


if __name__ == '__main__':
    app.run(debug=bool(app.config["FLASK_DEBUG"]), host=str(app.config["SERVER"]), port=app.config["PORT"])
