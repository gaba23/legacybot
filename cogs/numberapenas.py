import discord
from discord.ext import commands


class Numberapenas(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_message(self, message):
		print(message.content)
		if str(message.channel.id) == '823552109844365353':
			msg = message.content
			if msg.isdigit() == False:
				await message.delete()
	
def setup(bot):
	bot.add_cog(Numberapenas(bot))