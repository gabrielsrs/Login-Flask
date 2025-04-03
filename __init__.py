from src.app import app
from config import Config

if __name__ == '__main__':
    app.run(
        debug=Config.FLASK_DEBUG,
        host=Config.SERVER,
        port=Config.PORT,
    )
