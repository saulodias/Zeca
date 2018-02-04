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
        if ctx.author.nick:
            author = ctx.author.nick
        else:
            author = ctx.author.name
        if member.nick:
            member = member.nick
        else:
            member = member.name
        message = author + ' has banned ' + member + '.'
        await ctx.send(message)

    @commands.command(name='beijunda', aliases=['bd'])
    async def _beijunda(self, ctx, member: discord.Member):
        """Manda um beijunda para alguém."""
        if ctx.author.nick:
            author = ctx.author.nick
        else:
            author = ctx.author.name
        if member.nick:
            member = member.nick
        else:
            member = member.name
        message = author + ' mandou um beijunda para ' + member + '.'
        await ctx.send(message)


def setup(bot):
    bot.add_cog(Zoeira(bot))
