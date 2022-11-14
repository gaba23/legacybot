import discord
from discord.ext import commands

class Avatar(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def avatar(self, ctx, *, avamember: discord.Member=None):
        if not avamember: 
            avamember = ctx.message.author 
        userAvatar = avamember.avatar_url
        embedvar = discord.Embed(
            title = "Avatar de " + avamember.name,
            color = discord.Color.dark_blue()
        )
        embedvar.set_image(url='{}'.format(userAvatar))
        await ctx.send(embed=embedvar)

def setup(bot):
    bot.add_cog(Avatar(bot))