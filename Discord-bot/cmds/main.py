import discord
from discord.ext import commands
from core.classes import Cog_Extension


class Main(Cog_Extension):
    @commands.command()         # 輸入!ping bot會回覆你目前的延遲
    async def ping(self, ctx):   # ctx = context  包含(使用者, ID, 所在伺服器, 所在頻道)
        await ctx.send(f"{round(self.bot.latency*1000)} (ms)")

    @commands.command()
    async def hi(self, ctx):
        await ctx.send("Hello lisonkor.")

def setup(bot):
    bot.add_cog(Main(bot))