from requests import request
from app import app


class TwitterEndpoint:
    def __init__(self, token):
        self.token = token

    def info_user(self):
        url_endpoint = 'https://api.twitter.com/2/users/me'

        headers = {
            'authorization': f'Bearer {self.token["access_token"]}'
        }

        return request('GET', url_endpoint, headers=headers).json()


class TwitterOauth:
    def __init__(self, code):
        self.code = code

    def twitter_oauth(self):
        url_token = 'https://api.twitter.com/2/oauth2/token'

        payload_token = {
            'code': self.code['code'],
            'grant_type': 'authorization_code',
            'client_id': app.config['TWITTER_CID'],
            'redirect_uri': app.config['TWITTER_RURL'],
            'code_verifier': 'challenge'
        }
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        return request('POST', url_token, data=payload_token, headers=headers).json()
