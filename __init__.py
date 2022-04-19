from app import app


with app.app_context():
    from routes import handle

    app.register_blueprint(handle)


if __name__ == '__main__':
    app.run(
        debug=bool(app.config["FLASK_DEBUG"]),
        host=str(app.config["SERVER"]),
        port=app.config["PORT"]
    )
