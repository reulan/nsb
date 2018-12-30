"""
mpmsimo
2/12/2017

nsb.py - n00bshack Discord bot
"""
import json
import logging
import random

from discord.ext import commands
import discord

import api.ffxiv as ffxiv_api
import api.twitch as twitch_api
import api.warcraft as wow_api

logger = logging.getLogger('nsb')

# Discord API specific 
description = """noobshack discord bot"""
bot = commands.Bot(command_prefix='!', description=description)

# Discord bot command funtions
@bot.event
async def on_ready():
    logger.info('Logged into server:')
    logger.info(bot.user.name)
    logger.info(bot.user.id),

@bot.command()
async def roll(dice : str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await bot.say('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await bot.say(result)

@bot.command(description='For when you wanna settle the score some other way')
async def choose(*choices : str):
    """Chooses between multiple choices."""
    await bot.say(random.choice(choices))

@bot.command()
async def joined(member : discord.Member):
    """Says when a member joined."""
    await bot.say('{0.name} joined in {0.joined_at}'.format(member))

@bot.group(pass_context=True)
async def cool(ctx):
    """Says if a user is cool.

    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await bot.say('Yes, {0.subcommand_passed} is leet h4x0|2 aka cool.'.format(ctx))

# Load configuration
def load_credentials(filename):
    with open(filename) as f:
        return json.load(f)

# World of Warcraft API subcommands
def load_wow_api(apikey):
    logger.info('World of Warcraft API loaded as \'wa\'')
    wa = wow_api.WowAPI()
    wa.apikey = apikey
    return wa

@bot.group(pass_context=True)
async def wow(ctx):
    """World of Warcraft API extension."""
    if ctx.invoked_subcommand is None:
        await bot.say('Invalid wow commands given.')

# Add subcommands here
@wow.command(name='item')
async def item(itemId : str):
    """Prints item information associated with an itemId."""
    info = wa.get_item(itemId)
    await bot.say('Looking up item with ID: {iid}\n{itemInfo}'.format(iid=itemId, itemInfo=info))

if __name__ == '__main__':
    filepath = '/usr/bin/nsb/config/{c}'.format(c='credentials.json')
    credentials = load_credentials(filepath)
    bot.client_id = credentials['discord_client_id']
    bot.bots_key = credentials['discord_token']
    wa = load_wow_api(credentials['wow_apikey'])

    bot.run(bot.bots_key)
