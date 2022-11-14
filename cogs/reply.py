import discord
from discord.ext import commands

class Reply(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def reply(self, ctx, messageid: int, *, message):
        await ctx.message.delete()
        msg = await ctx.fetch_message(messageid)
        await msg.reply(message, mention_author=True)

def setup(bot):
    bot.add_cog(Reply(bot))