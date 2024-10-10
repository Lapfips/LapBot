# README file to explain the src/youtube folder

### Folder configuration:

In this folder you can find all the functions and class used to interacte with youtube and send the informations to discord. You can also find a text document that's saving the last youtube video id

- `youtube_bot.py`

  ##### This class is checking with the API if a new video has been upload and send the notification on discord if it's necessary. It's also writing in the youtube_message_id.txt file the youtube video id sended

- `youtube_api.py`

  ##### This class is using the youtube API to check the last upload video and return those informations

- `youtube_message_id.txt`

  ##### This file is saving the last youtube video id sended on discord to verify if it's the same as the last video id in the youtube data base
