# TD1-Discord-Python-Bot

### A Discord Bot written up by TwelfthDoctor1 that uses the disnake library (originally discord.py) to communicate with the Discord API.

## Project Note

This project is a **Work-In-Progress**, so not all expected features are available.

This project is open source to show the inner workings of the Sir Top Hat Bot used in TD1 Servers (token and data files not included).

## Getting Started

### Requirements

[comment]: <> (May plan on using a Command script to automate installation process.)

- Python 3.8 onwards
- disnake module library
- dotenv module library
- MasterApprentice Library (included in code)

To install disnake:

```commandline
[Quoted from disnake README]

# Linux/macOS
python3 -m pip install -U disnake

# Windows
py -3 -m pip install -U disnake
```

To install dotenv:
```commandline
pip install dotenv
```

To use this python repository as your discord bot, use `git clone` to clone the repository, alternatively you can directly download this code.

Before running the bot, you need to create a file called `Discord_Token.env`. The contents of the file should be as followes:

```commandline
DISCORD_TOKEN={TOKEN}

DEVELOPER_ID={DEVELOPERID}
```

**Make sure to replace those with `{}` with the correct values.**

To start up the bot (make sure that your shell is in the repository folder):
```commandline
[macOS/Linux]
python3 bot.py

[Windows]
py3 bot.py
```