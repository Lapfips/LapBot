# Discord Bot

This is a bot for Discord that tells you when a new YouTube video is up or when someone is streaming on Twitch. Pretty cool, right?

## Directory architecture

```
.
├── .gitignore
├── README.md
├── requirements.txt
│
├── config
│   └── .env
│
├── logs
│   └── bot.log
│
└── src
    ├── main.py
    ├── utils.py
    ├── __init__.py
    │
    ├── discord_rep
    │   ├── discord_api.py
    │   ├── discord_bot.py
    │   └── __init__.py
    │
    ├── twitch_rep
    │   ├── twitch_api.py
    │   ├── twitch_bot.py
    │   ├── twitch_message_id.txt
    │   └── __init__.py
    │
    ├── youtube_rep
    │   ├── youtube_api.py
    │   ├── youtube_bot.py
    │   ├── youtube_message_id.txt
    │   └── __init__.py
    │
    └── twitter_rep
        ├── twitter_api.py
        ├── twitter_bot.py
        ├── twitter_message_id.txt
        └── __init__.py

```

### You can find more explanation about each files in their own folder !
