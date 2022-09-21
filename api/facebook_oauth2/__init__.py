from requests import request
from app import app


class FacebookOauth:
    def __init__(self, code):
        self.code = code

    def token(self):
        url = 'https://graph.facebook.com/v15.0/oauth/access_token'

        params = {
            'client_id': app.config['FACEBOOK_CID'],
            'client_secret': app.config['FACEBOOK_CSECRET'],
            'redirect_uri': app.config['FACEBOOK_RURL'],
            'code': self.code['code']
        }

        return request('get', url, params=params).json()


class FacebookEndpoint:
    def __init__(self, token):
        self.token = token

    def user_name(self):
        url = 'https://graph.facebook.com/me'
        headers = {
            'authorization': f'Bearer {self.token["access_token"]}'
        }

        return request('get', url, headers=headers).json()
