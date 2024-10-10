# README file to explain the src/discord_rep folder

### Folder configuration:

In this folder you can find all the functions and class used to interacte with discord

- `discord_bot.py`

  ##### This class is used to ask to the API class to send a notification on the twitch channel or the youtube channel. This class can also update the twitch notifications if the stream informations change

- `discord_api.py`

  ##### This class is using the discord's API by sending messages in the channels or updating them. It's also used to create the embed messages and to get the last message id on the twitch discord's channel
