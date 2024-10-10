# README file to explain the src/twitch folder

### Folder configuration:

In this folder you can find all the functions and class used to interacte with twitch and send the informations to discord. You can also find a text document that's saving the last discord message id

- `twitch_bot.py`

  ##### This class is checking if the stream if alive and if it needs to send or update a notification. It's calling the twitch API functions to get stream informations

- `twitch_api.py`

  ##### This class is used to get access to the twitch and streams informations

- `twitch_message_id.txt`

  ##### This file is used to use the last discord message id to notify the discod message if it's needed
