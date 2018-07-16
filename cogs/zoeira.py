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
        
        author = ctx.author.display_name
        
        if member in ctx.message.mentions:
            target = member.display_name
        else:
            target = member.mention
        
        if author == member.display_name:
            message = ':hammer: | **' + author + \
            ' has hammered their thumb. What a shame.**'
        
        elif author == 'fausthanos':
            message = ':hammer: | **' + target + \
                ' has been slain by Fausthanos, for the good of the Universe.**'
                
        elif author == 'charon':
            message = ':hammer: | ** Charon has made a dinner reservation for ' + \
                target + '**'
            
        elif author == 'winston':
            message = ':hammer: | ** Winston has acted upon ' + \
                target + '\'s own actions.**'
        
        else:
            message = ':hammer: | **' + author + \
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
