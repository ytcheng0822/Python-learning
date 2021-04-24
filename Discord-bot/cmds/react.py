import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json

with open(file="setting.json", mode="r", encoding="utf-8") as jfile:
    jdata = json.load(jfile)

class React(Cog_Extension):    # React is a cog
    @commands.command()
    async def picture(self, ctx):
        random_pic = random.choice(jdata["Picture"])
        pic = discord.File(random_pic)
        await ctx.send(file=pic)

    @commands.command()
    async def url_picture(self, ctx):
        random_pic = random.choice(jdata["URL_Picture"])
        await ctx.send(random_pic)

def setup(bot):
    bot.add_cog(React(bot))     # add React cog
