import requests # type: ignore
import os

class TwitchAPI:
    def __init__(self):
        self.client_id = os.getenv('TWITCH_CLIENT_ID')
        self.client_secret = os.getenv('TWITCH_CLIENT_SECRET')
        self.user_login = os.getenv('TWITCH_USER_LOGIN')

    def get_access_token(self):
        url = 'https://id.twitch.tv/oauth2/token'
        params = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'grant_type': 'client_credentials'
        }
        response = requests.post(url, params=params)
        if response.status_code == 200:
            return response.json()['access_token']
        else:
            print("Erreur lors de la récupération du token d'accès Twitch.")
            return None

    def get_stream_info(self):
        access_token = self.get_access_token()
        if access_token:
            url = f'https://api.twitch.tv/helix/streams?user_login={self.user_login}'
            headers = {
                'Authorization': f'Bearer {access_token}',
                'Client-ID': self.client_id
            }
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                stream_data = response.json().get('data', [])
                return stream_data[0] if stream_data else None
            else:
                print("Erreur lors de la récupération des informations du stream.")
                return None
        return None
