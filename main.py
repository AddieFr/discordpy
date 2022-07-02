import discord
from discord.ext import commands
import datetime
import os
from urllib import parse, request
import re
import random



intents = discord.Intents.all() #need to enable
bot = commands.Bot(command_prefix='~', intents=intents)


for foldername in os.listdir('./cogs'): 
    for filename in os.listdir(foldername):
        if filename.endswith('.py') and not filename in ['util.py', 'error.py']: 
            bot.load_extension(f'cogs.{foldername}.{filename[:-3]}')


bot = commands.Bot(command_prefix='>', description="Shyizen-Maid")

@bot.command()
async def ping(ctx):
    await ctx.send('pong')



@bot.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="Shyizen parivte server for don't get a void server check <#961949738280841266>", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    # embed.set_thumbnail(url=f"{ctx.guild.icon}")
    embed.set_thumbnail(url="")

    await ctx.send(embed=embed)


# Events
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="Shyizen-Maid", url="http://www.twitch.tv/accountname"))
    print(bot.user.name + "is online now!")


@bot.listen()
async def on_message(message):
    if "Change this (any name)" in message.content.lower():
        await message.channel.send('')
        await bot.process_commands(message)




bot.run('OTkyMjY0NzYyNDI5ODA4Njcy.GKwa8i.LpLdZwOziPso9vCFquURAQDlOINWqVmaS2NW0s')