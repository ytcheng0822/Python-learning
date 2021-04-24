import discord
from discord.ext import commands
import json
import random
import os

with open(file="setting.json", mode="r", encoding="utf-8") as jfile:
    jdata = json.load(jfile)


intents = discord.Intents.all()  # 加入所有會用到的功能
bot = commands.Bot(command_prefix="!", intents=intents)  # 建立bot

@bot.event
async def on_ready():
    print(">> Bot is online <<")


@bot.command()
async def load(ctx, extension):
    bot.load_extension(f"cmds.{extension}")
    await ctx.send(f"Loaded {extension} done.")

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f"cmds.{extension}")
    await ctx.send(f"Unloaded {extension} done.")

@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(f"cmds.{extension}")
    await ctx.send(f"Reloaded {extension} done.")


for filename in os.listdir("./cmds"):
    if filename.endswith(".py"):
        bot.load_extension(f"cmds.{filename[:-3]}")  # 從開頭第0個字算起到結尾前3個字為止


if __name__ == "__main__":      # 加上if __name__ == "__main__":的原因，其實就是因為程式可能會有「單獨執行」與「被引用」兩種情形
    bot.run(jdata["TOKEN"])     # 加上 __name__ == "__main__" 的判斷即可讓檔案在被引用時，不該執行的程式碼不被執行