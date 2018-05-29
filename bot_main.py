###
### This bot needs python3.5 with modules discord.py and requests:
###
### sudo apt-get install python3 python3-pip
### sudo python3 -m pip install -U discord.py
### sudo python3 -m pip install -U requests
###
### Replace bot_token_here with your bot token.
###
### Start bot using:
### python3 bot_main.py
### 


import discord
from discord.ext.commands import Bot

startup_extensions = ["bot_cog"]

# Here you can modify the bot's prefix and description and wether it sends help in direct messages or not.
client = Bot(description="ASF-DiscordBot", command_prefix="!", pm_help = False)

@client.event
async def on_ready():
    print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
    print('Use this link to invite {}:'.format(client.user.name))
    print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(client.user.id))

    servers = client.servers

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            client.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

    client.run('bot_token_here')
