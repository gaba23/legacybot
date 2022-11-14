import discord
from discord.ext import commands
from uploads.img_dowload import ImageGet
import os

class SayLancamento(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
           
    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def saylancamento(self, ctx, chatid: str, *, msg):

        chatid = chatid.replace("<", "")
        chatid = chatid.replace(">", "")
        chatid = chatid.replace("#", "")
        file = ''
        
        canal = self.bot.get_channel(int(chatid))

        for attachment in ctx.message.attachments:
            print(attachment.url)
            print(attachment.filename)
            img = ImageGet(attachment.url,attachment.filename)
            img.Dowload()
            file = discord.File(os.path.join(attachment.filename))
            print(file)

        await canal.send(content=msg, file=file)

        for attachment in ctx.message.attachments:
            await os.remove(attachment.filename)


    @saylancamento.error
    async def saylancamento_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("você é fraco, lhe falta permissões para usar esse comando. <:itachi:828747684910989373>")
        
        

def setup(bot):
    bot.add_cog(SayLancamento(bot))