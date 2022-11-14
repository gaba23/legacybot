import discord
from discord.ext import commands


class Editapelido(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def editapelido(self, ctx,user: discord.Member=None, *, nome):
    	await ctx.message.delete()
    	await user.edit(nick=str(nome))
    @editapelido.error
    async def editapelido_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("você é fraco, lhe falta permissões para usar esse comando. <:itachi:828747684910989373>")
def setup(bot):
    bot.add_cog(Editapelido(bot))