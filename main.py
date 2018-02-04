import discord
import private
from cogs import utilities
from discord.ext import commands

command_prefix = '>'
description = """Portuguese Learning and Discussion utilities bot."""

bot = commands.Bot(command_prefix=command_prefix, description=description)

initial_extensions = ['cogs.moderator', 'cogs.utilities', 'cogs.zoeira']

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
    guild = bot.guilds[0]
    role = discord.utils.get(guild.roles, name='hitmeup')
    for member in role.members:
        await member.remove_roles(role)
        await member.send(utilities.Utilities.expired_role_msg)


@bot.event
async def on_member_join(member):
    general_channel = discord.utils.get(bot.get_all_channels(), name='general')
    info_channel = discord.utils.get(bot.get_all_channels(), name='info')

    welcome_message = 'Welcome, <@' + str(member.id) + '>! ' + \
        'Please check out <#' + str(info_channel.id) + '> to learn ' + \
        'about the server rules and cool stuff. :smile:'
    if general_channel is not None:
        await general_channel.send(welcome_message)


@bot.event
async def on_reaction_add(reaction, user):
    print('{}, {}, {}'.format(reaction, user, str(reaction.message.content)))


@bot.command(name='revoke_role', hidden=True)
@commands.is_owner()
async def _revoke_role(ctx, *, role):
    role = await commands.RoleConverter().convert(ctx, role)
    for member in role.members:
        await member.remove_roles(role)
        await member.send(utilities.Utilities.expired_role_msg)


@bot.command(name='eval', hidden=True)
@commands.is_owner()
async def _eval(ctx, *, code):
    """A bad example of an eval command"""
    await ctx.send(eval(code))

bot.run(private.__TOKEN)
