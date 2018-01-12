import discord
import asyncio
import private
import dicinformal
from discord.ext import commands

command_prefix = '>'
description = """Portuguese Learning and Discussion utilities bot."""

bot = commands.Bot(command_prefix=command_prefix, description=description)

@bot.event
async def on_ready():
    print('Logged in as: {}'.format(bot.user.name))
    print('ID: {}'.format(bot.user.id))
    print('Discord Version: {}'.format(discord.__version__))
    print('-------------')
    await bot.change_presence(game=discord.Game(name='Type >help'))


@bot.command(name='dicinf', aliases=['di', 'dicinformal'])
async def _dicionarioinformal(ctx, *, term=None):
    """
    Looks a word up in the Dicionário Informal.
    
    Don't trust this dictionary blindly. It's like a Brazilian Urban Dictionary.
    """
    result = dicinformal.Query(term)
    embed = discord.Embed(title=result.term,
                          url=result.url,
                          description=result.description,
                          color=0x3498DB)
    embed.set_footer(icon_url=result.favicon,
                     text=result.disclaimer)
    await ctx.send(embed=embed)
    
@_dicionarioinformal.error
async def _dicionarioinformal_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        await ctx.send(':exclamation: No results found.')

@bot.command(name='role', aliases=['r'])
async def _role(ctx, *, role):
    """
    Assigns or removes a role.
    
    If role is a level role (Level A, Level B, Level C, or Native),
    the previous level will be automatically removed.
    """
    level_roles = ['Level A', 'Level B', 'Level C', 'Native']
    country_roles = ['PT', 'BR', 'AO', 'CV', 'GQ', 'GW',
                     'MO', 'MZ', 'ST', 'TL']
    other_roles = ['hitmeup', 'Notify me']
    public_roles = [*level_roles, *country_roles, *other_roles]
    roles_validation = [i.lower() for i in public_roles]
    if role.lower() in roles_validation:
        role = public_roles[roles_validation.index(role)]
    else:
        raise commands.BadArgument    
    role = await commands.RoleConverter().convert(ctx, role)
    
    member = ctx.author
    if role in member.roles:
        await member.remove_roles(role)
        await ctx.send(':white_check_mark: Role removed.')
    elif role.name in public_roles:
        if role.name in level_roles:
            for q, r in enumerate(member.roles):
                if r.name in level_roles:
                    await member.remove_roles(r)
        await member.add_roles(role)
        await ctx.send(':white_check_mark: Role granted.')

@_role.error
async def _role_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send(':exclamation:This role does not exist or is not ' +
                       'public. Check your spelling.')
        
@bot.command()
async def nick(ctx, *, new_nick):
    """ Changes the nickname of a member. """
    member = ctx.author
    await member.edit(nick=new_nick)

@nick.error
async def nick_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        #await ctx.send(error.__cause__)
        await ctx.send('I don\'t have permission for that, master.')


@bot.command(name='eval', hidden=True)
@commands.is_owner()
async def _eval(ctx, *, code):
    """A bad example of an eval command"""
    await ctx.send(eval(code))

bot.run(private.__TOKEN)
