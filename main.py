import discord
import os
from dotenv import load_dotenv


bot = discord.Bot()

@bot.event
async def on_ready():
    print("Bot is online !")
    print(f"USER : {bot.user}")
    print(f"USER ID : {bot.user.id}")
    print("_________________________________")

cogs_list = [
    "tic",
    "clean",
    "ping"
    ]

for cog in cogs_list:
    bot.load_extension(f"Cogs.{cog}")

load_dotenv()
bot.run(os.getenv("TOKEN"))
