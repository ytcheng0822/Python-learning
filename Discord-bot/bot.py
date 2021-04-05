import discord
from discord.ext import commands
import json
import random

with open(file="setting.json", mode="r", encoding="utf-8") as jfile:
    jdata = json.load(jfile)


intents = discord.Intents.all()  # 加入所有會用到的功能
bot = commands.Bot(command_prefix="!", intents=intents)  # 建立bot

@bot.event
async def on_ready():
    print(">> Bot is online <<")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(int(jdata["Welcome_channel"]))
    await channel.send(f"{member} join!")    # member會依訪客名稱不同改變

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(int(jdata["Leave_channel"]))
    await channel.send(f"{member} leave!")

@bot.command()         # 輸入!ping bot會回覆你目前的延遲
async def ping(ctx):   # ctx = context  包含(使用者, ID, 所在伺服器, 所在頻道)
    await ctx.send(f"{round(bot.latency*1000)} (ms)")

@bot.command()
async def picture(ctx):
    random_pic = random.choice(jdata["Picture"])
    pic = discord.File(random_pic)
    await ctx.send(file=pic)

@bot.command()
async def url_picture(ctx):
    random_pic = random.choice(jdata["URL_Picture"])
    await ctx.send(random_pic)


bot.run(jdata["TOKEN"])