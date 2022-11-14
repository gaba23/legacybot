import discord
from discord.ext import commands

class EditembedFile(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def editembedfile(self, ctx,channel: discord.TextChannel, msgID: int, cor: str):
        mensagem = await channel.fetch_message(msgID)
        embedvar = discord.Embed(
            color=int(cor,16),
        )
        for attachment in ctx.message.attachments:
            embedvar.set_image(url=attachment.url)
        await mensagem.edit(embed=embedvar)
    
    @editembedfile.error
    async def editembedfile_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("você é fraco, lhe falta permissões para usar esse comando. <:itachi:828747684910989373>")

def setup(bot):
    bot.add_cog(EditembedFile(bot))