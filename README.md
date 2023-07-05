# faw-bot

faw-bot is a very simple discord bot with some basic commands. 
my favourite command is the `oj` command which gives the current and historical prices of orange juice.

## Features

- oj

## Installation

### Requirements

- Python 3.6 or higher
- discord.py library

### Steps

1. Clone the repository.

    ```bash
    git clone https://github.com/faw01/faw-bot.git
    ```

2. Go to the project directory.

    ```bash
    cd faw-bot
    ```

3. Install the requirements.

    ```bash
    pip install --U -r requirements.txt
    ```

4. Add your bot token.

   Open the `bot_token.py` file and replace `'REDACTED'` with your bot token. If you don't have one, you can create a bot in the Discord Developer Portal.

5. Run the bot.

    ```bash
    python main.py
    ```

Your bot should now be up and running!

## Commands

- `/faw hello` - responds with 'Hello, World!'
- `/faw info` - sends an embedded message containing information.
- `/faw ping` - responds with latency in milliseconds.
- `/faw oj` - you know what it does.
