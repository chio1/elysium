import discord
import asyncio
import openpyxl
import os

client = discord.Client()

@client.event
async def on_ready():
    print('온')
    print('------')
    game = discord.Game("!명령어 l 제작중")
    await client.change_presence(status=discord.Status.online , activity=game)

@client.event
async def on_message(message):
    if message.content.startswith("!명령어"):
        await message.channel.send(embed=discord.Embed(title="제작중", description= " \n\n\n차후 추가 예정", color=0x00ff00))


access_token = os.environ["BOT_TOKEN"]
client.run(access_token)