import discord
from discord.ext import commands


class Ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(name = "ban", description = "Ban a member")
    @discord.default_permissions(administrator = True, ban_members = True)
    async def ban(self, ctx, pseudo, reason):
        await ban

def setup(bot):
    bot.add_cog(Ban(bot))