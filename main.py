import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='.', intents=intents)

@bot.event
async def on_ready():
    print('Online')
    print(bot.user.name)
    print(bot.user.id)
    print('---libus---')
    await bot.change_presence(status=discord.Status.dnd,activity=discord.Activity(type=discord.ActivityType.watching, name="O sal salvar o mundo"))


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(str(os.getenv('token')))
