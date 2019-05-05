###
###
### Replace bot_master_here with your Discord ID. (right click on your avatar in Developer mode).
### If you set a IPC password, replace ?password=null with ?password=yourpassword
###
###
import discord
from discord.ext.commands import Bot
from discord.ext import commands

# Needs python3-requests
import requests

class Asf(commands.Cog):

	def __init__(self, bot):
		self.bot = bot
		self.url_base = "http://127.0.0.1:1242/Api/Command/"
		self.ipc_pass = "?password=null"
		pass

	def get (self, params):
		"""API access"""
		url = "{url_base}{params}{ipc_pass}".format(url_base = self.url_base, params = params, ipc_pass = self.ipc_pass)

		print (url)

		try:
			r = requests.post(url, timeout=30)
		except requests.exceptions.RequestException as e:  # This is the correct syntax
			return "Erreur : " + str(e)
		json_res = r.json()
		response = "Message : " + json_res["Message"] + "\n```\n" + json_res["Result"] + "\n```"
		return response

	#@commands.listen()
	@commands.Cog.listener()
	async def on_message(self,message):
		if ( message.content[0] == "!" and message.author.id == bot_master_here):
			args = message.content[1:].replace(" ","%20")

			async with message.channel.typing():
				response = self.get(args)
				try:
					await message.channel.send(response)
				except:
					await message.channel.send("Message too long")


def setup(bot):
	bot.add_cog(Asf(bot))
