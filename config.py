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

