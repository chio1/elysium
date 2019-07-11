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
    role = discord.utils.get(message.guild.roles , name= "뉴비도우미")
    if message.content.startswith("!명령어"):
        await message.channel.send(embed=discord.Embed(title="명령어", description= " \n\n\n차후 추가 예정", color=0x00ff00))

    if message.content.startswith("!인증"):
        author = message.guild.get_member(int(message.content[4:22]))
        role = discord.utils.get(message.guild.roles , name = "인증 회원")
        await author.add_roles(role)
        await message.channel.send(embed=discord.Embed(title="명령어",
                                                       description=" 인증완료입니다",
                                                       color=0x00ff00))

    if message.content.startswith("!취소인증"):
        author = message.guild.get_member(int(message.content[6:24]))
        role = discord.utils.get(message.guild.roles, name="인증 회원")
        await author.remove_roles(role)
        await message.channel.send(embed=discord.Embed(title="명령어",
                                                       description=" 인증취소입니다.",
                                                       color=0x00ff00))


access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
