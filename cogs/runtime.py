import discord
from datetime import datetime
from discord.ext import commands

class Runtime(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	global starttime

	starttime = datetime.utcnow()

	@commands.command()
	async def runtime(self, ctx):
		now = datetime.utcnow()
		elapsed = now - starttime
		seconds = elapsed.seconds
		minutes, seconds = divmod(seconds, 60)
		hours, minutes = divmod(minutes, 60)
		uptime = '🗓️ {} dias\n🗓️ {} horas\n🗓️ {} minutos\n🗓️ {} segundos'.format(elapsed.days, hours, minutes, seconds)
		embed=discord.Embed(title="Tempo de atividade 🕰️", description="**Estou online há:**\n" + uptime, color=0x640202)
		embed.set_thumbnail(url="https://imgur.com/WZMylbw.gif")
		await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Runtime(bot))