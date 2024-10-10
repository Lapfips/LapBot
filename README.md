# Discord Bot

This is a bot for Discord that tells you when a new YouTube video is up or when someone is streaming on Twitch. Pretty cool, right?

## What You Need

### Directory Thingy

here’s the file stuff:

```md
.
├── [\*.gitignore](./.gitignore)
├── [README.md](./README.md)
├── [requirements.txt](./requirements.txt)
│
├── config
│ └── [.env](./config/.env)
│
├── logs
│ └── [bot.log](./logs/bot.log)
│
└── src
├── [main.py](./src/main.py)
├── [utils.py](./src/utils.py)
├── [**init**.py](./src/__init__.py)
│
├── discord_rep
│ ├── [discord_api.py](./src/discord_rep/discord_api.py)
│ ├── [discord_bot.py](./src/discord_rep/discord_bot.py)
│ └── [**init**.py](./src/discord_rep/__init__.py)
│
├── twitch
│ ├── [twitch_api.py](./src/twitch/twitch_api.py)
│ ├── [twitch_bot.py](./src/twitch/twitch_bot.py)
│ ├── [twitch_message_id.txt](./src/twitch/twitch_message_id.txt)
│ └── [**init**.py](./src/twitch/__init__.py)
│
└── youtube
├── [youtube_api.py](./src/youtube/youtube_api.py)
├── [youtube_bot.py](./src/youtube/youtube_bot.py)
├── [youtube_message_id.txt](./src/youtube/youtube_message_id.txt)
└── [**init**.py](./src/youtube/__init__.py)
```

### `.env` File in `config`

- **Discord Stuff**: `DISCORD_TOKEN`, `DISCORD_CHANNEL_ID_TWITCH`, `DISCORD_CHANNEL_ID_YOUTUBE`
- **Twitch Stuff**: `TWITCH_CLIENT_ID`, `TWITCH_CLIENT_SECRET`, `TWITCH_USER_LOGIN`, `TWITCH_URL`
- **Twitter Stuff**: You know, like `TWITTER_API_KEY`, `TWITTER_API_KEY_SECRET`, all those keys.
- **YouTube Stuff**: Same as above but for YouTube.

## File Stuff Explained

### `config`

#### `.env`

This is where you put your secret keys and stuff that lets you talk to the APIs or whatever.

### `logs`

#### `bot.log`

This is the log file. It’s got everything the bot does, but like, who really reads it anyway?

### `src`

#### `main.py`

The main thing that runs the whole bot every minute. Like, seriously, who thought this was a good idea?

#### `utils.py`

This has some random functions for logging and reading/writing files. Not sure why you’d need this, but it’s here.

#### `discord_rep`

##### `discord_bot.py`

This is the class that does the notifying or something for Discord.

##### `discord_api.py`

This handles the API requests to Discord. Simple enough.

### `youtube`

##### `youtube_bot.py`

This class checks if new videos are up or whatever. If so, it does its thing.

##### `youtube_api.py`

Just queries YouTube for video info. Super exciting, right?

##### `youtube_message_id.txt`

Keeps track of the last video ID so we don’t annoy people with double notifications. I guess that’s good?

### `twitch`

##### `twitch_bot.py`

This class checks if someone is live on Twitch and sends notifications.

##### `twitch_api.py`

Gets info from Twitch about live stuff.

##### `twitch_message_id.txt`

Stores Discord message ID or something for live notifications. Whatever.

### `requirements.txt`

Use `pip install -r requirements.txt` to get the packages you need. Easy peasy.
