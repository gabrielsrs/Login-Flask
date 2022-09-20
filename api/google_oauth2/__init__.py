from requests import request
from app import app


class GoogleOauth:
    def __init__(self, code):
        self.code = code

    def token(self):
        url = 'https://oauth2.googleapis.com/token'
        params = {
            'client_id': app.config['GOOGLE_CID'],
            'client_secret': app.config['GOOGLE_CSECRET'],
            'code': self.code['code'],
            'grant_type': 'authorization_code',
            'redirect_uri': app.config['GOOGLE_RURL']
        }
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        return request('post', url, data=params, headers=headers).json()


class GoogleEndpoint:
    def __init__(self, token):
        self.token = token

    def user_name(self):
        url = 'https://www.googleapis.com/userinfo/v2/me'
        headers = {
            'authorization': f'Bearer {self.token["access_token"]}'
        }

        return request('get', url, headers=headers).json()
