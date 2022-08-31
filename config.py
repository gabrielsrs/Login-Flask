from dotenv import load_dotenv
from os import getenv, path

load_dotenv(path.realpath('.env'))


class Config:
    """Load variables"""
    TESTING = getenv('TESTING')
    FLASK_DEBUG = getenv('FLASK_DEBUG')
    SECRET_KEY = getenv('SECRET_KEY')
    SERVER = getenv('SERVER')
    PORT = getenv('PORT')
    DAYS = getenv('DAYS')
    SQLALCHEMY_DATABASE_URI = getenv("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = getenv("SQLALCHEMY_TRACK_MODIFICATIONS")
    CLIENT_ID = getenv('CLIENT_ID')
    TWITTER_URL = getenv('TWITTER_URL')
