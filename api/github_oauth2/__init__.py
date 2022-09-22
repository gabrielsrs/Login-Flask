from requests import request
from app import app


class GithubOauth:
    def __init__(self, code):
        self.code = code

    def token(self):
        url = 'https://github.com/login/oauth/access_token'
        params = {
            'client_id': app.config['GITHUB_CID'],
            'client_secret': app.config['GITHUB_CSECRET'],
            'code': self.code['code'],
            'redirect_uri': app.config['GITHUB_RURL']
        }
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json'
        }

        return request('post', url, data=params, headers=headers).json()


class GithubEndpoint:
    def __init__(self, token):
        self.token = token

    def user_name(self):
        url = 'https://api.github.com/user'
        headers = {
            'authorization': f'Bearer {self.token["access_token"]}'
        }

        return request('get', url, headers=headers).json()
