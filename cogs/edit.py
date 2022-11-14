import discord
from discord.ext import commands

class Edit(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def edit(self, ctx, msgID: int, *, message):
        await ctx.message.delete()
        msg = await ctx.fetch_message(msgID)
        await msg.edit(content=message)

    @edit.error
    async def edit_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("você é fraco, lhe falta permissões para usar esse comando. <:itachi:828747684910989373>")
def setup(bot):
    bot.add_cog(Edit(bot))