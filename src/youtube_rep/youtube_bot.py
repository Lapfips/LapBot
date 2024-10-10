from .youtube_api import YoutubeAPI
from discord_rep.discord_bot import DiscordBot # type: ignore
from utils import FileManager # type: ignore

class YoutubeBot:
    def __init__(self):
        self.youtube_api = YoutubeAPI()
        self.discord_bot = DiscordBot()
        self.last_video_id_file = 'src/youtube/youtube_message_id.txt'

    def check_latest_video(self):
        last_video_id = FileManager.read_file(self.last_video_id_file)
        video_info = self.youtube_api.get_latest_video()

        if video_info:
            video_id = video_info['id'].get('videoId')
            if video_id and video_id != last_video_id:
                self.discord_bot.notify_youtube()
                FileManager.write_file(self.last_video_id_file, video_id)
