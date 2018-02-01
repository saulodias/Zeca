import discord
from discord.ext import commands
import asyncio


class Zoeira:
    """The zuera never ends."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ban', aliases=[])
    async def _ban(self, ctx, member: discord.Member):
        """For the craic."""
        message = str(ctx.author.nick) + " has banned " + str(member.nick) + '.'
        await ctx.send(message)

    @commands.command(name='beijunda', aliases=['bd'])
    async def _beijunda(self, ctx, member: discord.Member):
        """Manda um beijunda para alguém."""
        message = str(ctx.author.nick) + " mandou um beijunda para " + \
            str(member.nick) + '. :peach:'
        await ctx.send(message)


def setup(bot):
    bot.add_cog(Zoeira(bot))
