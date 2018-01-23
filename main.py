import discord
import private
from discord.ext import commands

command_prefix = '>'
description = """Portuguese Learning and Discussion utilities bot."""

bot = commands.Bot(command_prefix=command_prefix, description=description)

initial_extensions = ['cogs.moderator', 'cogs.utilities']

if __name__ == "__main__":
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as ex:
            print('Failed to load extension ' + extension)


@bot.event
async def on_ready():
    print('Logged in as: {}'.format(bot.user.name))
    print('ID: {}'.format(bot.user.id))
    print('Discord Version: {}'.format(discord.__version__))
    print('-------------')
    await bot.change_presence(game=discord.Game(name='Type >help'))


@bot.command(name='eval', hidden=True)
@commands.is_owner()
async def _eval(ctx, *, code):
    """A bad example of an eval command"""
    await ctx.send(eval(code))

bot.run(private.__TOKEN)
