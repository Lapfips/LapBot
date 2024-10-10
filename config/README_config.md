# README file to explain the config folder

### Environement variable in the .env file:

To use the bot your need to add the config/.env file and to add those informations inside

- **Discord**:
  - `DISCORD_TOKEN`,
  - `DISCORD_CHANNEL_ID_TWITCH`,
  - `DISCORD_CHANNEL_ID_YOUTUBE`
- **Twitch**:
  - `TWITCH_CLIENT_ID`,
  - `TWITCH_CLIENT_SECRET`,
  - `TWITCH_USER_LOGIN`,
  - `TWITCH_URL`
- **Twitter**:
  - `TWITTER_API_KEY`,
  - `TWITTER_API_KEY_SECRET`,
  - `TWITTER_ACCESS_TOKEN`,
  - `TWITTER_ACCESS_TOKEN_SECRET`,
  - `TWITTER_USERNAME`,
  - `TWITTER_BEARER_TOKEN`,
  - `TWITTER_CLIENT_ID`,
  - `TWITTER_CLIENT_SECRET`
- **YouTube**:
  - `YOUTUBE_URL`,
  - `YOUTUBE_CHANNEL_ID`,
  - `YOUTUBE_API_KEY`

### Python packages needed by the bot:

In the `requirement.txt` file your can find every packages needed by the bot and install them with the `pip install -r config/requirements.txt` command in the main folder
