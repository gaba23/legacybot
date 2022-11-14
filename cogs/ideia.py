import discord
from discord.ext import commands

class Ideia(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ideia(self, ctx, *, message):
        user = self.bot.get_user(ctx.message.author.id)
        await ctx.message.delete()
        embedvar = discord.Embed(
            color=0x800000,
            description= message
        )
        msg = await ctx.send(embed=embedvar)

        await msg.add_reaction("<:check:828709725876125697>")
        await msg.add_reaction("<:nao:828715020505841705>")

def setup(bot):
    bot.add_cog(Ideia(bot))