import discord
from discord.ext import commands
import re
import json
import os

class EmojisToJson(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def emojistojson(self, ctx, *,emojis):
        data = []
        custom_emojis = re.findall(r'<:\w*:\d*>', emojis)
        custom_emojis = [int(e.split(':')[2].replace('>', '')) for e in custom_emojis]
        custom_emojis = [discord.utils.get(ctx.guild.emojis, id=e) for e in custom_emojis]
        for e in custom_emojis:
            data.append({'title': str(e.name),'image': str(e.url)})
        
        with open('macaco.json', 'w') as f:
            json.dump(data, f, ensure_ascii=False)
        
        await ctx.channel.send(content="Tá aí, eu tenho mais oque fazer <@"+ str(ctx.message.author.id) + ">", file=discord.File('macaco.json'))
        os.remove("macaco.json") 

    @commands.command()
    async def allemojistojson(self, ctx):
        data = []
        custom_emojis = ctx.guild.emojis
        for e in custom_emojis:
            data.append({'title': str(e.name),'image': str(e.url)})
        
        with open('macaco.json', 'w') as f:
            json.dump(data, f, ensure_ascii=False)
        
        await ctx.channel.send(content="Tá aí, eu tenho mais oque fazer <@"+ str(ctx.message.author.id) + ">", file=discord.File('macaco.json'))
        os.remove("macaco.json") 
        
        

def setup(bot):
    bot.add_cog(EmojisToJson(bot))