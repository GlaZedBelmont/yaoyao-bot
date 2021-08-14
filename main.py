# Bot cog template - Dynamic cog loading template.
# Copyright (C) 2018 - Valentijn "noirscape" V.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License, version 2 as published by
# the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program. If not, see <http://www.gnu.org/licenses/>.

import yaml
from discord.ext import commands
import os
import os
import traceback
import sys

from traceback import format_exception, format_exc

'''Bot framework that can dynamically load and unload cogs.'''

config = yaml.safe_load(open('config.yml'))
secure = yaml.safe_load(open('secure.yml'))
bot = commands.Bot(command_prefix=commands.when_mentioned_or(
    config['prefix']),
    description='')

bot.loaded_cogs = []
bot.unloaded_cogs = []


bot.load_extension("jishaku")

def check_if_dirs_exist():
    '''Function that creates the "cogs" directory if it doesn't exist already'''
    os.makedirs('cogs', exist_ok=True)

def load_autoload_cogs():
    '''
    Loads all .py files in the cogs subdirectory that are in the config file as "autoload_cogs" as cogs into the bot. 
    If your cogs need to reside in subfolders (ie. for config files) create a wrapper file in the cogs 
    directory to load the cog.
    '''
    for entry in os.listdir('cogs'):
        if entry.endswith('.py') and os.path.isfile('cogs/{}'.format(entry)) and entry[:-3] in config['autoload_cogs']:
            try:
                bot.load_extension("cogs.{}".format(entry[:-3]))
                bot.loaded_cogs.append(entry[:-3])
            except Exception as e:
                print(e)
            else:
                print('Succesfully loaded cog {}'.format(entry))

def get_names_of_unloaded_cogs():
    '''
    Creates an easy loadable list of cogs.
    If your cogs need to reside in subfolders (ie. for config files) create a wrapper file in the auto_cogs
    directory to load the cog.
    '''
    for entry in os.listdir('cogs'):
        if entry.endswith('.py') and os.path.isfile('cogs/{}'.format(entry)) and entry[:-3] not in bot.loaded_cogs:
            bot.unloaded_cogs.append(entry[:-3])

check_if_dirs_exist()
load_autoload_cogs()
get_names_of_unloaded_cogs()

@bot.command()
async def list_cogs(ctx):
    '''Lists all cogs and their status of loading.'''
    cog_list = commands.Paginator(prefix='', suffix='')
    cog_list.add_line('**✅ Succesfully loaded:**')
    for cog in bot.loaded_cogs:
        cog_list.add_line('- ' + cog)
    cog_list.add_line('**❌ Not loaded:**')
    for cog in bot.unloaded_cogs:
        cog_list.add_line('- ' + cog)
    
    for page in cog_list.pages:
        await ctx.send(page)

@bot.command()
async def membercount(ctx):
    """How many peeps do we have in here?"""
    await ctx.send(f'{ctx.guild} has {ctx.guild.member_count:,} peeps!')
    
# Error Handler
@bot.event
async def on_command_error(ctx, error):
        
    ignored = (commands.CommandNotFound)
    error = getattr(error, 'original', error)
    
    errorchannel = ctx.guild.get_channel(config['error_channels'][ctx.guild.id])
    
    if not errorchannel:
        errorchannel = ctx.channel
    
    if isinstance(error, ignored):
        return

    elif isinstance(error, commands.DisabledCommand):
        return await ctx.send(f'{ctx.command} has been disabled.')

    elif isinstance(error, commands.MissingRole):
        try:
            return await ctx.send(f'{ctx.author.mention}, you are missing the role {missing_role} .')
        except:
            pass

    elif isinstance(error, commands.NoPrivateMessage):
        try:
            return await ctx.author.send(f'{ctx.command} can not be used in DMs.')
        except:
            pass

    elif isinstance(error, commands.MissingRequiredArgument):
        try:
            return await ctx.send(f'{ctx.author.mention} **Missing Argument:** {error.param.name}.\n') and await ctx.send_help(ctx.command)
        except:
            pass

    elif isinstance(error, commands.CheckFailure):
        try:
            if ctx.guild.id == '632566001980145675':
                pass
            return await ctx.send(f"You don't have the permission to run ```{ctx.command.qualified_name}```")
        except:
            pass

    elif isinstance(error, commands.CommandOnCooldown):
        try:
            return await ctx.send(f"You're on cooldown, try again in {error.retry_after:.2f}s")
        except:
            pass

    elif isinstance(error, commands.BadArgument):
        if ctx.command.qualified_name == 'tag list':
            return await ctx.send('I could not find that member. Please try again.')

    msg = "".join(format_exception(type(error), error, error.__traceback__))
    await errorchannel.send(f"```{msg}```")
    
@bot.event
async def on_ready():
    print('----------')
    print('Logged in as:')
    print(bot.user.name)
    print(bot.user.id)
    print('----------')

bot.run(secure["token"])
