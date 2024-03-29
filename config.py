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
    TWITTER_CID = getenv('TWITTER_CID')
    TWITTER_URL = getenv('TWITTER_URL')
    TWITTER_RURL = getenv('TWITTER_RURL')
    TWITCH_CID = getenv('TWITCH_CID')
    TWITCH_URL = getenv('TWITCH_URL')
    TWITCH_RURL = getenv('TWITCH_RURL')
    TWITCH_CSECRET = getenv('TWITCH_CSECRET')
    GOOGLE_CID = getenv('GOOGLE_CID')
    GOOGLE_URL = getenv('GOOGLE_URL')
    GOOGLE_RURL = getenv('GOOGLE_RURL')
    GOOGLE_CSECRET = getenv('GOOGLE_CSECRET')
    FACEBOOK_CID = getenv('FACEBOOK_CID')
    FACEBOOK_URL = getenv('FACEBOOK_URL')
    FACEBOOK_RURL = getenv('FACEBOOK_RURL')
    FACEBOOK_CSECRET = getenv('FACEBOOK_CSECRET')
    GITHUB_CID = getenv('GITHUB_CID')
    GITHUB_URL = getenv('GITHUB_URL')
    GITHUB_RURL = getenv('GITHUB_RURL')
    GITHUB_CSECRET = getenv('GITHUB_CSECRET')
