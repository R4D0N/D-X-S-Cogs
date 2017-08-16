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
import time
import random

pulse = 0

class Ressurect:
    """Ressurect Something"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def Ressurect(self, ctx, *, ded:str):
    
        try:
            await self.bot.delete_message(ctx.message)
        except:
            pass
    
        await self.bot.say("Attempting to ressurect {}".format(ded))
        time.sleep(1)
        await self.bot.say("Shocking... Clear!")
        pulse = (random.randint(1, 2))
        if pulse == 1:
            await self.bot.say("Unsuccessful, trying again")
            time.sleep(1)
            await self.bot.say("Shocking... Clear!")
            pulse = (random.randint(1, 2))
            if pulse == 1:
                await self.bot.say("Unsuccessful, trying again")
                time.sleep(1)
                await self.bot.say("Shocking... Clear!")
                pulse = (random.randint(1, 2))
                if pulse == 1:
                    await self.bot.say("Unsuccessful, I'm sorry but {} has died".format(ded))
        
                else:
                    time.sleep(1)
                    await self.bot.say("{} has been recovered!".format(ded))
        
            else:
                time.sleep(1)
                await self.bot.say("{} has been recovered!".format(ded))
        
        else:
            time.sleep(1)
            await self.bot.say("{} has been recovered!".format(ded))
            
        
        

    
def setup(bot):
    bot.add_cog(Ressurect(bot))