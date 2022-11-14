import discord, asyncio
from discord.ext import commands

class Apagar(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def apagar(self, ctx, limit: int):
        if limit <= 666:
            limit = limit + 1
            await ctx.channel.purge(limit=limit)
            await ctx.send('Apagado por {}'.format(ctx.author.mention))
            await ctx.message.delete()
        else:
            await ctx.send("só posso apagar no maximo 666 mensagens por vez")
    
    @apagar.error
    async def apagar_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("você é fraco, lhe falta permissões para usar esse comando. <:itachi:828747684910989373>")

def setup(bot):
    bot.add_cog(Apagar(bot))