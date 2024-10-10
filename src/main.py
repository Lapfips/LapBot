import time
from twitch_rep.twitch_bot import TwitchBot
from youtube_rep.youtube_bot import YoutubeBot
from utils import Logger # type: ignore

def main():
    Logger.setup_logger()
    twitch_bot = TwitchBot()
    youtube_bot = YoutubeBot()

    while True:
        twitch_bot.check_stream_status()
        youtube_bot.check_latest_video()
        time.sleep(30)

if __name__ == "__main__":
    main()
