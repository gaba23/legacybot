import discord
import re
from discord.ext import commands


class Fake(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def fake(self, ctx, userid: str, *, message):
        await ctx.message.delete()
        userid = re.sub('[^0-9]', '', userid)
        webhooks = await ctx.message.channel.webhooks()
        naotem = True
        server = ctx.message.guild
        user = self.bot.get_user(int(userid))
        print(user)
        for member in server.members:
            if member.id == int(userid):
                user = member
        for webhook in webhooks:
            if(webhook.name == "boteco"):
                try:
                    if user.nick == None:
                        await webhook.send(content=message, username=user.name ,avatar_url=user.avatar_url)
                    else:
                        await webhook.send(content=message, username=user.nick ,avatar_url=user.avatar_url)
                except:
                    await webhook.send(content=message, username=user.name ,avatar_url=user.avatar_url)
                naotem = False
        if naotem:
            webhook = await ctx.message.channel.create_webhook(name="boteco")
            try:
                if user.nick == None:
                    await webhook.send(content=message, username=user.name ,avatar_url=user.avatar_url)
                else:
                    await webhook.send(content=message, username=user.nick ,avatar_url=user.avatar_url)
            except:
                await webhook.send(content=message, username=user.name ,avatar_url=user.avatar_url)
       # await webhook.delete()


def setup(bot):
    bot.add_cog(Fake(bot))