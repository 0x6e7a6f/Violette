import discord
from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(name = "ping", description = "Show Bot latency")
    async def ping(self, ctx):
        latency = round(self.bot.latency, 5) * 1000
        await ctx.respond("Latency : " + str(latency) + " ms") # Can't add emoji :bomb:

def setup(bot):
    bot.add_cog(Ping(bot))