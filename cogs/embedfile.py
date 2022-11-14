import discord
from discord.ext import commands

class Embedfile(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
           
    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def embedfile(self, ctx, chatid: str,color):

        chatid = chatid.replace("<", "")
        chatid = chatid.replace(">", "")
        chatid = chatid.replace("#", "")
        
        canal = self.bot.get_channel(int(chatid))
        embedvar = discord.Embed(
            color=int(color,16),
        )
        for attachment in ctx.message.attachments:
            embedvar.set_image(url=attachment.url)

        await canal.send(embed=embedvar)

    @embedfile.error
    async def embedfile_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("você é fraco, lhe falta permissões para usar esse comando. <:itachi:828747684910989373>")
        
        

def setup(bot):
    bot.add_cog(Embedfile(bot))