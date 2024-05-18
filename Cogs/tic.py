import discord
from discord.ext import commands


class Tic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(name = "tic", description = "Tic... Tac... BOOOOOM")
    async def tic(self, ctx):
        await ctx.respond("Tac !")

def setup(bot):
    bot.add_cog(Tic(bot))
