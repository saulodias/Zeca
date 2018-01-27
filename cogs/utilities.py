import discord
import dicinformal
import asyncio
from discord.ext import commands


class Utilities:
    """Member utilities."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='role', aliases=['r'])
    async def _role(self, ctx, *, role):
        """
        Assigns or removes a role.

        If role is a level role (Level A, Level B, Level C, or Native),
        the previous level will be automatically removed.

        The role 'hitmeup' expires after 1 hour.

        Sub-command:
            list:  Shows a list of public roles.
        """
        level_roles = {'level a': 'Level A', 'level b': 'Level B',
                       'level c': 'Level C', 'native': 'Native'}
        country_roles = {'pt': 'PT', 'br': 'BR', 'ao': 'AO', 'cv': 'CV', 'gq': 'GQ',
                         'gw': 'GW', 'mo': 'MO', 'mz': 'MZ', 'st': 'ST', 'tl': 'TL'}
        other_roles = {'hitmeup': 'hitmeup', 'notify me': 'Notify me'}
        public_roles = {**level_roles, **country_roles, **other_roles}

        if role.lower() in list(public_roles.keys()):
            role = public_roles[role.lower()]
            role = await commands.RoleConverter().convert(ctx, role)
            member = ctx.author
            if role in member.roles:
                await member.remove_roles(role)
                await ctx.send(':white_check_mark: Role removed.')
            else:
                if role.name in list(level_roles.values()):
                    for _, r in enumerate(member.roles):
                        if r.name in list(level_roles.values()):
                            await member.remove_roles(r)
                await member.add_roles(role)
                await ctx.send(':white_check_mark: Role granted.')
                # Schedules the hitmeup role expiration
                if role.name == 'hitmeup':
                    expired_role_msg = 'Your role "hitmeup" role has ' + \
                        'expired. To renew the role type `>r hitmeup` ' + \
                        'in the bot_channel. Don\'t forget this role ' + \
                        'expires each hour.\nThanks for being part of the ' +\
                        'Portuguese Learning and Discussion Community! :smile:'
                    await asyncio.sleep(3600)
                    if role in member.roles:
                        await member.remove_roles(role)
                        await ctx.author.send(expired_role_msg)

        elif role == 'list':
            output = 'Public roles available:\n' + '```' + \
                     ', '.join(list(public_roles.values())) + '```'
            await ctx.send(output)
        else:
            raise commands.BadArgument

    @_role.error
    async def _role_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send(':exclamation:This role does not exist or is not ' +
                           'public. Check your spelling.')

    @commands.command(name='dicinf', aliases=['di', 'dicinformal'])
    async def _dicionarioinformal(self, ctx, *term):
        """
        Looks a word up in the Dicionário Informal.

        Don't trust this dictionary blindly. It's like a Brazilian Urban Dictionary.
        """

        def _meaning(entry):
            result = dicinformal.Query(entry)
            embed = discord.Embed(title=result.term,
                                  url=result.url,
                                  description=result.description,
                                  color=0x3498DB)
            embed.set_footer(icon_url=result.favicon,
                             text=result.disclaimer)
            return embed

        def _synonym(entry):
            return 'synonym of {}'.format(entry)

        def _antonym(entry):
            return 'antonym of {}'.format(entry)

        # Parse sub-command
        sub_commands = {'-a': _antonym, '-s': _synonym}
        sub_command = [i for i in term if i in list(sub_commands.keys())]
        if sub_command:
            sub_command = sub_command[0]
            term = list(term)
            term.remove(sub_command)
            term = ' '.join(term)
            await ctx.send(sub_commands[sub_command](term))
        # Default command
        else:
            term = ' '.join(term)
            await ctx.send(embed=_meaning(term))

    @_dicionarioinformal.error
    async def _dicionarioinformal_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            # await ctx.send(error.__cause__)
            await ctx.send(':exclamation: No results found.')

    @commands.command()
    async def nick(self, ctx, *, new_nick):
        """ Changes the nickname of a member. """
        member = ctx.author
        await member.edit(nick=new_nick)

    @nick.error
    async def nick_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            # await ctx.send(error.__cause__)
            await ctx.send('I don\'t have permission for that, master.')


def setup(bot):
    bot.add_cog(Utilities(bot))
