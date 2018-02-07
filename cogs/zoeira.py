import discord
from discord.ext import commands
import asyncio


class Zoeira:
    """The zuera never ends."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ban', aliases=[])
    async def _ban(self, ctx, *, member: discord.Member):
        """For the craic."""

        if member in ctx.message.mentions:
            target = member.display_name
        else:
            target = member.mention

        message = ':hammer: | **' + ctx.author.display_name + \
            ' has banned ' + target + '**.'

        await ctx.send(message)

    @commands.command(name='beijunda', aliases=['bd'])
    async def _beijunda(self, ctx, *, member: discord.Member):
        """Manda um beijunda para alguém."""

        if member in ctx.message.mentions:
            target = member.display_name
        else:
            target = member.mention

        message = ':kiss::peach: | **' + ctx.author.display_name + \
            ' mandou um beijunda para ' + target + '**.'

        await ctx.send(message)


def setup(bot):
    bot.add_cog(Zoeira(bot))
