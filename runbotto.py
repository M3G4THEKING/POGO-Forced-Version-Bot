import discord
from discord.ext import commands
import logging
import requests


client = discord.Client()

@client.event
async def on_ready():
    print("Connected!")
    print("Logged in as: " + client.user.name)
    print("User ID:" + client.user.id)
    print("_________________")
    await client.change_presence(game=discord.Game(name="!version"))

logging.basicConfig(level=logging.ERROR)
bot = commands.Bot(command_prefix='!')

@client.event
async def on_message(message):
    if message.content.startswith("!version"):
        def version_check(msg):
            return msg.content.startswith("!version")
        message = await client.wait_for_message(author=None, check=version_check)
        res = requests.get('https://pgorelease.nianticlabs.com/plfe/version')
        await client.send_message(message.channel, ("```\nCurrently Forced API: " + (res.text) + "```"))

client.run("------Insert Bot Token Here------")
