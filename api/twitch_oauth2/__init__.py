from requests import request
from app import app


class TwitchLogin:
    def __init__(self, code):
        self.code = code

    def token(self):
        url = 'https://id.twitch.tv/oauth2/token'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        params = {
            'client_id': app.config['TWITCH_CID'],
            'client_secret': app.config['TWITCH_CSECRET'],
            'code': self.code['code'],
            'grant_type': 'authorization_code',
            'redirect_uri': app.config['TWITCH_RURL']
        }

        return request('POST', url, data=params, headers=headers).json()

    @staticmethod
    def refresh_token(refresh):
        url = 'https://id.twitch.tv/oauth2/token'
        params = {
            'client_id': app.config['TWITCH_CID'],
            'client_secret': app.config['TWITCH_CSECRET'],
            'refresh_token': refresh['refresh_token'],
            'grant_type': 'refresh_token',
        }
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        return request('POST', url, data=params, headers=headers).json()

    @staticmethod
    def revoke(token):
        url = 'https://id.twitch.tv/oauth2/revoke'
        params = {
            'client_id': app.config['TWITCH_CID'],
            'token': token['access_token'],
        }
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        return request('POST', url, data=params, headers=headers)


class TwitchEndpoint:
    def __init__(self, token):
        self.token = token

    def user_name(self):
        url = 'https://api.twitch.tv/helix/users'
        headers = {
            'authorization': f"Bearer {self.token['access_token']}",
            'client-id': app.config['TWITCH_CID']
        }

        result = request('GET', url, headers=headers)

        return result.json()
