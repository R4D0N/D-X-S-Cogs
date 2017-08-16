#Created by X3N0N#4459
#Co-founder of D X S cogs

from discord.ext import commands
from .utils.chat_formatting import box
from .utils.dataIO import dataIO
from .utils import checks
from __main__ import user_allowed, send_cmd_help
from copy import deepcopy
import os
import discord

class MirrorMessage:
    """Speak Through Your Bot"""

    def __init__(self, bot):
        self.bot = bot

    @checks.admin_or_permissions(manage_server=True)
    @commands.command(pass_context=True)
    async def MM(self, ctx, *, msg:str):
        """[P]MM [what you want to say]"""
        fmt = "\u200B{}".format(msg)
        await self.bot.say(fmt)
        try:
            await self.bot.delete_message(ctx.message)
        except:
            pass
    
def setup(bot):
    bot.add_cog(MirrorMessage(bot))
