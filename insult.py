import discord
from discord.ext import commands
from .utils.chat_formatting import escape_mass_mentions, italics, pagify
from random import randint
from random import choice
from enum import Enum
from urllib.parse import quote_plus
from cogs.utils.dataIO import dataIO
import datetime
import time
import aiohttp
import asyncio
#import random
import os
from random import choice as randchoice
import textwrap
import math
from copy import copy
try:
    from PIL import Image, ImageDraw, ImageFont, ImageColor
    pil_available = True
except:
    pil_available = False


class insult:
    """Poii's Insult cog."""

    def __init__(self, bot):
        self.bot = bot
        self.insults = dataIO.load_json('data/insult/insults.json') #Calls the insult JSON
        self.count = dataIO.load_json('data/insult/insults.json')


    @commands.command(pass_context=True)
    async def insult(self, context, user : discord.Member):
        """Insult <user>"""

        insults = dataIO.load_json('data/insult/insults.json') #Defines the JSON file into the command.
        
        await self.bot.say(user.mention + '**{}** {}'.format(randchoice(self.insults['msg2']), randchoice(self.insults['msg3']))) #Let's make some people buttmad.



    @commands.command(pass_context=True)
    async def lovemeter(self, ctx):
        """How much does Poiibot love you?"""

        count = dataIO.load_json('data/insult/insults.json') #Defines the JSON file into the command.

        author = ctx.message.author

        await self.bot.say(author.mention + ", According to the meter index, Poiibot loves you a total of **{}**%. :3".format(randchoice(self.count['lovemeter'])))




def setup(bot):
    n = insult(bot)
    bot.add_cog(n)