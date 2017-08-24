#Created by X3N0N#4459
#Co-founder of D X S cogs

import discord
from discord.ext import commands
from .utils.dataIO import fileIO
from .utils import checks
from __main__ import send_cmd_help
import os
import time
from time import gmtime, strftime
import sqlite3

class Cdict:
    """Allows users to define things."""

    def __init__(self, bot):
        self.bot = bot
        LexPath = "data/Cdict/Lexicon"
        table_name = "Lexicon"
        id_column = "ID"
        Sid_column = "SID"
        Key_column = "Key"
        Val_column = "Value"
        Uid_column = "UID"
        Date_column = "Date"
    
    @checks.admin_or_permissions(manage_server=True)
    @commands.command(pass_context=True)
    async def define(self, ctx, name:str, definition:str):
        """[P]define "word" <meaning>"""

        #Definition saving
        LexPath = "data/Cdict/Lexicon"
        table_name = "Lexicon"
        id_column = "ID"
        Sid_column = "SID"
        Key_column = "Key"
        Val_column = "Value"
        Uid_column = "UID"
        Date_column = "Date"
        server = ctx.message.server
        ServerID = server.id
        author = ctx.message.author
        AuthorID = author.id
        DT = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
        conn = sqlite3.connect(LexPath)
        c = conn.cursor()
        

        #Checking and potentially writing
        try:
            c.execute('INSERT INTO Lexicon (SID, Key, Value, UID, Date) VALUES (?, ?, ?, ?, ?)', (ServerID, name, definition, AuthorID, DT))
            await self.bot.say("{} Successfully added to the database!".format(name))
        except sqlite3.IntegrityError:
            await self.bot.say("```You already have a definition for {}.```".format(name))

            
        conn.commit()
        conn.close()
    @checks.admin_or_permissions(manage_server=True)    
    @commands.command(pass_context=True)
    async def undefine(self, ctx, name:str):
        """[P]undefine "word" """
        
        #Definition Erasing
        LexPath = "data/Cdict/Lexicon"
        table_name = "Lexicon"
        id_column = "ID"
        Sid_column = "SID"
        Key_column = "Key"
        Val_column = "Value"
        Uid_column = "UID"
        Date_column = "Date"
        server = ctx.message.server
        ServerID = server.id
        author = ctx.message.author
        AuthorID = author.id
        DT = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
        conn = sqlite3.connect(LexPath)
        c = conn.cursor()
        try:
            c.execute ("DELETE FROM Lexicon Where SID = ? and Key = ?", (ServerID, name,))
            await self.bot.say("{} Successfully removed from the database!".format(name))
        except sqlite3.IntegrityError:
            await self.bot.say("```ERROR: ID doesn't exist in PRIMARY KEY column {}```".format(id_column))
        
        conn.commit()
        conn.close()
        
    @commands.command(pass_context=True)
    async def whatis(self, ctx, name:str):
        """[P]whatis "word" """    
        #Definition Querying
        LexPath = "data/Cdict/Lexicon"
        table_name = "Lexicon"
        id_column = "ID"
        Sid_column = "SID"
        Key_column = "Key"
        Val_column = "Value"
        Uid_column = "UID"
        Date_column = "Date"
        server = ctx.message.server
        ServerID = server.id
        author = ctx.message.author
        AuthorID = author.id
        DT = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
        conn = sqlite3.connect(LexPath)
        c = conn.cursor()
        
        #Gathering
        c.execute("SELECT Value FROM Lexicon WHERE SID = ? and key = ?", (ServerID, name,))
        
        all_rows = c.fetchone()
        if all_rows:
            Result = all_rows[0]
            thedata = ("{Q}: {R}".format(Q = name, R = Result))
            data = discord.Embed(description=thedata, colour=discord.Colour(0x9400D3))
            await self.bot.say(embed=data)
            
        else:
            await self.bot.say("```ERROR: ID doesn't exist in PRIMARY KEY column {}```".format(id_column))
          
        conn.commit()
        conn.close()
        
#Insuring Data folder        
def check_folders():
    if not os.path.exists("data/Cdict"):
        print("Creating data/Cdict folder...")
        os.makedirs("data/Cdict")

#Insuring Data files        
def check_files():
    LexPath = "data/Cdict/Lexicon"
    if not os.path.exists(LexPath):
        # open connection to a sqlite file object
        conn = sqlite3.connect(LexPath)
        c = conn.cursor()

        # creating a new SQLite table & Index
        c.execute('CREATE TABLE Lexicon (ID INTEGER PRIMARY KEY, SID INTEGER, Key TEXT, Value TEXT, UID INTEGER, Date TEXT)')
        c.execute('CREATE UNIQUE INDEX "main"."Index of Lexicon" ON "Lexicon" ("SID" ASC, "Key" ASC)')


        # commit changes and close the connection to the sqlite file object.
        conn.commit()
        conn.close()

def setup(bot):
    check_folders()
    check_files()
    bot.add_cog(Cdict(bot))

