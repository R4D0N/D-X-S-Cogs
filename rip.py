import discord
from discord.ext import commands
from .utils.dataIO import fileIO
from .utils.dataIO import dataIO
from .utils import checks
import asyncio
import textwrap
import os
import math
import aiohttp
from copy import copy

try:
    from PIL import Image, ImageDraw, ImageFont, ImageColor

    pil_available = True
except:
    pil_available = False


class rip:
    """rest in pieces"""

    def __init__(self, bot):
        self.bot = bot
        self.drawing_settings = fileIO("data/rip/settings.json", "load")

    @commands.command(pass_context=True)
    async def rip(self, ctx, user: discord.Member=None):
        """rip <user>"""
        text = "Rest in Peace,\n {}".format(user.name)
        text2 = user.name
        result = Image.open('data/rip/stone.jpg').convert('RGBA')
        process = Image.new('RGBA', (833, 576), (0, 0, 0))
        fnt = ImageFont.truetype('data/rip/animeace.otf', 45)
        fnt_sm = ImageFont.truetype('data/rip/animeinept.otf', 40)
        d = ImageDraw.Draw(process)
        sign = user.name
        author_width = fnt_sm.getsize("— " + sign)[0]
        d.rectangle([(0, 0), (833, 576)], fill=(0, 0, 0, 0))
        d.text((140, 200), text, font=fnt, fill="#2f3642")
        #d.rectangle((25, 25), ava)
        #d.text((200 - author_width - 25, 65), "— " + sign, font=fnt_sm, fill="#000000")
        #d.rectangle([(10, 10), (390, 90)], fill=None, outline=(200, 200, 200, 128))
        result = Image.alpha_composite(result, process)
        result.save('data/rip/temp.png', 'PNG', quality=100)
        await self.bot.send_file(ctx.message.channel, 'data/rip/temp.png')
        os.remove('data/rip/temp.png')

def setup(bot):
    # check_folders()
    # check_files()
    n = rip(bot)
    bot.add_cog(n)