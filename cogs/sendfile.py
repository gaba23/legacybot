import discord
from discord.ext import commands

class Sendfile(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@commands.command(pass_context=True)
	@commands.has_permissions(administrator=True)
	async def file(self, ctx, chatid: str):
		chatid = chatid.replace("<", "")
		chatid = chatid.replace(">", "")
		chatid = chatid.replace("#", "")
		canal = self.bot.get_channel(int(chatid))
		for attachment in ctx.message.attachments:
			await canal.send(attachment.url)

	@file.error
	async def file_error(self, ctx, error):
		if isinstance(error, commands.MissingPermissions):
			await ctx.send("você é fraco, lhe falta permissões para usar esse comando. <:itachi:828747684910989373>")

def setup(bot):
	bot.add_cog(Sendfile(bot))