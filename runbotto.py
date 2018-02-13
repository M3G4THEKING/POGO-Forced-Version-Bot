import discord
from discord.ext import commands
import logging
import requests
import time


bot = commands.Bot(command_prefix='!')

logging.basicConfig(level=logging.ERROR)

@bot.command(pass_context=True)
async def version(ctx):
    if ctx:
        res = requests.get('https://pgorelease.nianticlabs.com/plfe/version')
        await bot.say("```\nCurrently Forced API: " + (res.text) +
                      "\n\nSuccesfully requested Niantic Labs at:\n" +
                      str(time.asctime() + "```"))

bot.run("------Insert Bot Token Here------")
