import requests # type: ignore
import os

class YoutubeAPI:
    def __init__(self):
        self.api_key = os.getenv('YOUTUBE_API_KEY')
        self.channel_id = os.getenv('YOUTUBE_CHANNEL_ID')

    def get_latest_video(self):
        url = f'https://www.googleapis.com/youtube/v3/search?key={self.api_key}&channelId={self.channel_id}&part=snippet,id&order=date&maxResults=1'
        response = requests.get(url)

        if response.status_code == 200:
            video_data = response.json()
            if video_data['items']:
                return video_data['items'][0]
            else:
                print("Aucune vidéo trouvée.")
                return None
        else:
            print(f"Erreur lors de la récupération de la vidéo YouTube: {response.status_code}")
            return None
