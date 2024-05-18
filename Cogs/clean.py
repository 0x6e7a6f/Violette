import discord
from discord.ext import commands


class Clean(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(name = "clean", description = "Delete the number of messages you wish (limit at 100).")
    async def clean(self, ctx, number):

        try:
            convertedNumber = int(number)
        except:
            await ctx.respond("You didn't enter a number. Please, try again. ", ephemeral = True)
            return

        if convertedNumber > 100:
            response = await ctx.respond("The limit is 100 messages. Please, choose a smaller number.", ephemeral = True)
            await response.delete_original_response(delay=5)
            return

        messages = await ctx.channel.history(limit = convertedNumber).flatten()
        await ctx.channel.delete_messages(messages)
        response = await ctx.respond(str(len(messages)) + " messages deleted.", ephemeral = True)
        await response.delete_original_response(delay = 5)


def setup(bot):
    bot.add_cog(Clean(bot))
