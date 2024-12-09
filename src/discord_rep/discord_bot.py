from .discord_api import DiscordAPI
from utils import FileManager
import os

class DiscordBot:
    def __init__(self):
        self.discord_api = DiscordAPI()
        self.last_message_id_file = 'src/twitch/twitch_message_id.txt'

    def notify_twitch(self):
        channel_id = os.getenv('DISCORD_CHANNEL_ID_TWITCH')
        message = self.discord_api.create_embed_twitch_message()
        return self.discord_api.send_message(channel_id, message)
    
    def update_notif_twitch(self):
        channel_id = os.getenv('DISCORD_CHANNEL_ID_TWITCH')
        message = self.discord_api.create_embed_twitch_end_message()
        return self.discord_api.modify_message(channel_id, message, FileManager.read_file(self.last_message_id_file))

    def notify_youtube(self):
        channel_id = os.getenv('DISCORD_CHANNEL_ID_YOUTUBE')
        message = self.discord_api.create_embed_youtube_message()
        return self.discord_api.send_message(channel_id, message)
