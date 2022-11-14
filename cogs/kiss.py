import discord
from discord.ext import commands
from random import randint

class Kiss(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def kiss(self, ctx, kiss: discord.Member=None):
        user = self.bot.get_user(ctx.message.author.id)
        await ctx.message.delete()
        if not kiss: 
            await ctx.send('lembre-se de mencionar um usuário válido para beijar!')
        else:
            embedvar = discord.Embed(
                title= user.name + " beijou " + kiss.name,
                color=0x800000
            )


            aleatorio = randint(0,7)

            if(aleatorio == 0):
                embedvar.set_image(url="https://media.giphy.com/media/3uhDOBLjDX5yDNXr3x/giphy.gif")
            elif(aleatorio == 1):
                embedvar.set_image(url="https://loritta.website/assets/img/actions/kiss/female_x_male/gif_378.gif")
            elif(aleatorio == 2):
                embedvar.set_image(url="https://media.giphy.com/media/lnLTjmGU7qt0Ams20V/giphy.gif")
            elif(aleatorio == 3):
                embedvar.set_image(url="https://i.imgur.com/4Ad9iwh.gif")
            elif(aleatorio == 4):
                embedvar.set_image(url="https://pa1.narvii.com/6942/4e2885141812813b051d187a82b628c1dc4b0326r1-500-281_hq.gif")
            elif(aleatorio == 5):
                embedvar.set_image(url="https://media.giphy.com/media/l4FsKa1n9fyStiwZW/giphy.gif")
            elif(aleatorio == 6):
                embedvar.set_image(url="https://gifimage.net/wp-content/uploads/2018/10/anime-peck-gif-5.gif")
            elif(aleatorio == 7):
                embedvar.set_image(url="https://loritta.website/assets/img/actions/kiss/female_x_female/gif_348.gif")

            await ctx.send(embed=embedvar)

def setup(bot):
    bot.add_cog(Kiss(bot))