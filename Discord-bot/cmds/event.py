import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json

with open(file="setting.json", mode="r", encoding="utf-8") as jfile:
    jdata = json.load(jfile)


class Event(Cog_Extension):
    @commands.Cog.listener()    # commands.Cog.listener = bot.event
    async def on_member_join(self, member):            # member(成員)
        channel = self.bot.get_channel(int(jdata["Welcome_channel"]))
        await channel.send(f"{member} join!")    # member會依訪客名稱不同改變

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(int(jdata["Leave_channel"]))
        await channel.send(f"{member} leave!")

    @commands.Cog.listener()
    async def on_message(self, msg):
        keyword = jdata["Keyword"]
        if msg.content in keyword and msg.author != self.bot.user:     # 如果輸入的訊息有在list當中
            await msg.channel.send("Hi")                               # bot就會在該頻道回應Hi



def setup(bot):
    bot.add_cog(Event(bot))