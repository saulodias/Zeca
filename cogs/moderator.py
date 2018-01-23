import discord
from discord.ext import commands


class Moderator:
    """Moderator command utilities."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        """A ping function for moderators."""
        await ctx.send('pong')

    async def __local_check(self, ctx):
        """A local check for moderator role."""
        if not isinstance(ctx.channel, discord.abc.GuildChannel):
            return False

        role = discord.utils.get(ctx.author.roles, name='Mod')
        return role is not None

    async def __error(self, ctx, error):
        """Cog error handling."""
        print('Error in {0.command.qualified_name}: {1}'.format(ctx, error))
        await ctx.send('You do not have the necessary permission.')


def setup(bot):
    bot.add_cog(Moderator(bot))
