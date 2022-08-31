from requests import request
from app import app

class Endpoint:
    def __init__(self, token):
        self.token = token

    def info_user(self):
        url_endpoint = 'https://api.twitter.com/2/users/me'

        headers = {
            'authorization': f'Bearer {self.token}'
        }

        data_user = request('GET', url_endpoint, headers=headers).json()

        return data_user


class TwitterOauth:
    def __init__(self, state_code):
        self.state_code = state_code

    def twitter_oauth(self):
        url_token = 'https://api.twitter.com/2/oauth2/token'

        payload_token = {
            'code': self.state_code['code'],
            'grant_type': 'authorization_code',
            'client_id': app.config['CLIENT_ID'],
            'redirect_uri': app.config['REDIRECT_URL'],
            'code_verifier': 'challenge'
        }
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        user_token = request('POST', url_token, data=payload_token, headers=headers).json()['access_token']

        return user_token
