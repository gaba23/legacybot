import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('Online')
    print(client.user.name)
    print(client.user.id)
    print('---libus---')

@client.event
async def on_message(message):
    if message.content.lower().startswith('.marca'):
        if str(message.author.id) == "198240622023409665":
            number = "<@680807378635194389>"
            while(True):
                await asyncio.sleep(1)
                await message.channel.send(number)

client.run('')
