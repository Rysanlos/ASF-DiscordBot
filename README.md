# ASF-DiscordBot

[![Discord](https://img.shields.io/badge/Discord-chat-brightgreen.svg)](https://discord.gg/bdnQ44M)
[![Python](https://img.shields.io/badge/Python-3.5-blue.svg)](https://pypi.python.org/)
[![ASF release](https://img.shields.io/github/release/JustArchi/ArchiSteamFarm.svg?label=ASF&maxAge=600)](https://github.com/JustArchi/ArchiSteamFarm/releases/latest)
[![GitHub License](https://img.shields.io/github/License/LeO-Fr/ASF-DiscordBot.svg)](https://github.com/LeO-Fr/ASF-DiscordBot/blob/master/LICENSE)


## Requirements

* Python 3.5+
* discord.py
* requests

## Installation

```shell
sudo apt-get install python3 python3-pip
sudo python3 -m pip install -U discord.py
sudo python3 -m pip install -U requests
git clone https://github.com/LeO-Fr/ASF-DiscordBot.git
cd ASF-DiscordBot
```

## Configuration

```
In bot_main.py: Replace bot_token_here with your bot token.
In bot_cog.py: Replace bot_master_here with your Discord ID. (right click on your avatar in Developer mode).
In bot_cog.py: If you set a IPC password, replace ?password=null with ?password=yourpassword
```

## Run

```shell
python3 bot_main.py
```