import random
import logging
import json

import discord
from discord.ext import commands

import wowapi
import cmd_info

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

description = """Noobshack discord bot."""

bot = commands.Bot(command_prefix='!', description=description)

@bot.event
async def on_ready():
    print('Logged into server:')
    print(bot.user.name)
    print(bot.user.id),

# World of Warcraft API subcommands
@bot.group(pass_context=True)
async def wow(ctx):
    """Command helper for the World of Warcraft API."""
    if ctx.invoked_subcommand is None:
        await bot.say(info.wow_api_help)

@cool.command(name='item')
async def _bot():
    """Is the bot cool?"""
    await bot.say('Of course, nsb is legit!!!')

@bot.command()
async def wow(wow_command_list):
    await bot.say("wow test")

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
async def repeat(times : int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await bot.say(content)

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
        await bot.say('No, {0.subcommand_passed} is not cool'.format(ctx))

@cool.command(name='nsb')
async def _bot():
    """Is the bot cool?"""
    await bot.say('Of course, nsb is legit!!!')

def load_credentials():
    with open('credentials.json') as f:
        return json.load(f)

if __name__ == '__main__':
    credentials = load_credentials()
    bot.client_id = credentials['client_id']
    bot.bots_key = credentials['token']

    bot.run(bot.bots_key)

    handlers = log.handlers[:]
    for hdlr in handlers:
        hdlr.close()
        log.removeHandler(hdlr)
