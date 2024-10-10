import requests # type: ignore
import os
import discord # type: ignore
from twitch.twitch_api import TwitchAPI # type: ignore
from youtube.youtube_api import YoutubeAPI # type: ignore
from utils import FileManager  # type: ignore

class DiscordAPI:
    def __init__(self):
        self.token = os.getenv('DISCORD_TOKEN')
        self.last_message_id_file = 'src/twitch/twitch_message_id.txt'
        self.user_login = os.getenv('TWITCH_USER_LOGIN')
        self.youtube_api = YoutubeAPI()
        self.twitch_api = TwitchAPI()
        self.channel_id = os.getenv('DISCORD_CHANNEL_ID_TWITCH')

    def send_message(self, channel_id, embed=None):
        url = f'https://discord.com/api/v9/channels/{channel_id}/messages'
        headers = {
            'Authorization': f'Bot {self.token}',
            'Content-Type': 'application/json'
        }
        
        data = {}
        if embed:
            data['embeds'] = [embed.to_dict()]
        
        response = requests.post(url, headers=headers, json=data)

        if response.status_code == 200:
            FileManager.write_file(self.last_message_id_file, self.get_last_message_id_twitch(self.channel_id))
            return True
        else:
            print(f"Erreur lors de l'envoi de la notification : {response.status_code}, {response.text}")
            return False
        

    def modify_message(self, channel_id, embed, last_message_id):
        print(f"Modifying message with ID: {last_message_id} in channel: {channel_id}")
        
        url = f'https://discord.com/api/v9/channels/{channel_id}/messages/{last_message_id}'
        headers = {
            'Authorization': f'Bot {self.token}',
            'Content-Type': 'application/json'
        }

        data = {}
        if embed:
            data['embeds'] = [embed.to_dict()]

        response = requests.patch(url, headers=headers, json=data)

        if response.status_code == 200:
            print("L'embed a été remplacé avec succès.")
            print(f"Réponse API : {response.json()}")  # Affiche le contenu de la réponse
            return True
        elif response.status_code == 404:
            print(f"Erreur 404 : Le message avec l'ID {last_message_id} n'existe pas dans ce canal.")
        else:
            print(f"Erreur lors de la modification du message : {response.status_code}, {response.text}")
        
        return False


    
    def create_embed_twitch_message(self):
        stream_info = self.twitch_api.get_stream_info()
        
        if stream_info:
            streamer_name = stream_info['user_name']
            stream_title = stream_info['title']
            game_name = stream_info['game_name']
            viewer_count = stream_info['viewer_count']
            stream_url = f"https://twitch.tv/{self.user_login}"
            thumbnail_url = stream_info['thumbnail_url'].format(width=320, height=180)

            embed = discord.Embed(
                title=f"{streamer_name} est en live maintenant!",
                description=f"**{stream_title}**\nEn train de jouer à: {game_name}",
                color=0x9146FF
            )
            embed.add_field(name="Spectateurs", value=str(viewer_count), inline=True)
            embed.add_field(name="Regarder le stream", value=f"[Clique ici pour regarder!]({stream_url})", inline=True)
            embed.set_thumbnail(url=thumbnail_url)
            embed.set_footer(text="Twitch", icon_url="https://www.twitch.tv/favicon.ico")
            return embed
        else:
            return None

    def create_embed_youtube_message(self):
        video_info = self.youtube_api.get_latest_video()
        
        if video_info:
            video_title = video_info['snippet']['title']
            channel_name = video_info['snippet']['channelTitle']
            video_id = video_info['id']['videoId']
            video_url = f"https://youtu.be/{video_id}"
            thumbnail_url = video_info['snippet']['thumbnails']['high']['url']

            embed = discord.Embed(
                title=f"Nouvelle vidéo de {channel_name}",
                description=f"**{video_title}**",
                color=0xFF0000
            )
            embed.add_field(name="Regarder la vidéo", value=f"[Clique ici pour regarder!]({video_url})", inline=True)
            embed.set_thumbnail(url=thumbnail_url)
            embed.set_footer(text="YouTube", icon_url="https://www.youtube.com/favicon.ico")
            return embed
        else:
            return None
        
    def create_embed_twitch_end_message(self):
        video_info = self.youtube_api.get_latest_video()

        if video_info:
            video_id = video_info['id']['videoId']
            video_url = f"https://youtu.be/{video_id}"
            thumbnail_url = video_info['snippet']['thumbnails']['high']['url']

            embed = discord.Embed(
                title=f"{self.user_login} n'est plus en live!",
                description=f"Tu peux retrouver ma dernière vidéo grâce au lien ci-dessous",
                color=0x9146FF
            )
            embed.add_field(name="Regarder la vidéo", value=f"[Clique ici pour regarder!]({video_url})", inline=True)
            embed.set_thumbnail(url=thumbnail_url)
            embed.set_footer(text="YouTube", icon_url="https://www.youtube.com/favicon.ico")
            return embed
        else:
            return None
        
    def get_last_message_id_twitch(self, channel_id):
        url = f'https://discord.com/api/v9/channels/{channel_id}/messages?limit=1'
        headers = {
            'Authorization': f'Bot {self.token}'
        }
        
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            messages = response.json()
            if messages:
                last_message_id = messages[0]['id']
                return last_message_id
            else:
                print("Aucun message trouvé dans ce canal.")
                return None
        else:
            print(f"Erreur lors de la récupération des messages : {response.status_code}, {response.text}")
            return None
