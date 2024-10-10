from .twitch_api import TwitchAPI
from discord_rep.discord_bot import DiscordBot
from discord_rep.discord_api import DiscordAPI
from utils import FileManager

class TwitchBot:
    def __init__(self):
        self.twitch_api = TwitchAPI()
        self.discord_bot = DiscordBot()
        self.discord_api = DiscordAPI()
        self.is_streaming = False
        self.last_message_id_file = 'src/twitch/twitch_message_id.txt'

    def check_stream_status(self):
        stream_info = self.twitch_api.get_stream_info()
        if stream_info and stream_info['title'] != 'Pas de stream actif':
            if not self.is_streaming:
                self.discord_bot.notify_twitch()
                self.is_streaming = True
        else:
            if self.is_streaming:
                self.discord_bot.update_notif_twitch()
                self.is_streaming = False
