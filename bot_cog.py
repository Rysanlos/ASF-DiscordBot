###
###
### Replace bot_master_here with your Discord ID. (right click on your avatar in Developer mode).
###
###
import discord
from discord.ext.commands import Bot
from discord.ext import commands

# Needs python3-requests
import requests

class Asf:

    def __init__(self, bot):
        self.bot = bot
        self.url_base = "http://127.0.0.1:1242/Api/Command/"
        pass
        
    def get (self, name, param=None):
        """API access"""
        if (param != None):
            url = "{url_base}{name}%20{param}".format(url_base = self.url_base, name = name, param = param)
        else:
            url = "{url_base}{name}".format(url_base = self.url_base, name = name)
        
        print (url)
        
        try:
            r = requests.post(url, timeout=10)
        except requests.exceptions.RequestException as e:  # This is the correct syntax
            return "Erreur : " + str(e)
        json_res = r.json()
        response = "Message : " + json_res["Message"] + "\n```\n" + json_res["Result"] + "\n```"
        return response
 
    #@commands.listen()
    async def on_message(self,message):
        if ( message.content[0] == "!" and message.author.id == "bot_master_here"):
            args = message.content[1:].split(" ")
            if args == []:
                return
                
            name = args[0]
            if len(args) > 1:
                param = args[1]
            else:
                param = None
                
            await self.bot.send_typing(message.channel)
            response = self.get(name, param)
            try:
                await self.bot.send_message(message.channel, response)
            except:
                await self.bot.send_message(message.channel, "Message too long.")
            
    
def setup(bot):
    bot.add_cog(Asf(bot))
