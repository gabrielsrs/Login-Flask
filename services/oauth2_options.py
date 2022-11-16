from api.twitter_oauth2 import TwitterEndpoint, TwitterOauth
from api.twitch_oauth2 import TwitchLogin, TwitchEndpoint
from api.google_oauth2 import GoogleOauth, GoogleEndpoint
from api.facebook_oauth2 import FacebookOauth, FacebookEndpoint
from api.github_oauth2 import GithubOauth, GithubEndpoint


class Options:
    def __init__(self, social_type, code):
        self.social_type = social_type
        self.code = code

    def social(self):
        if self.social_type == 'twitter':
            token = TwitterOauth(self.code).twitter_oauth()
            username = TwitterEndpoint(token).info_user()

            return username['data']['name']

        elif self.social_type == 'twitch':
            token = TwitchLogin(self.code).token()
            username = TwitchEndpoint(token).user_name()

            return username['data'][0]['display_name']

        elif self.social_type == 'google':
            token = GoogleOauth(self.code).token()
            username = GoogleEndpoint(token).user_name()

            return username['name']

        elif self.social_type == 'facebook':
            token = FacebookOauth(self.code).token()
            username = FacebookEndpoint(token).user_name()

            return username['name']

        elif self.social_type == 'github':
            token = GithubOauth(self.code).token()
            username = GithubEndpoint(token).user_name()

            return username['login']
