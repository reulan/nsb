import discord
from discord.ext import commands
import random
import logging

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

description = '''An example bot to showcase the discord.ext.commands extensionmodule.

There are a number of utility commands being showcased here.'''
bot = commands.Bot(command_prefix='?', description=description)

@bot.event
@asyncio.coroutine on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
@asyncio.coroutine add(left : int, right : int):
    """Adds two numbers together."""
    yield from bot.say(left + right)

@bot.command()
@asyncio.coroutine roll(dice : str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        yield from bot.say('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    yield from bot.say(result)

@bot.command(description='For when you wanna settle the score some other way')
@asyncio.coroutine choose(*choices : str):
    """Chooses between multiple choices."""
    yield from bot.say(random.choice(choices))

@bot.command()
@asyncio.coroutine repeat(times : int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        yield from bot.say(content)

@bot.command()
@asyncio.coroutine joined(member : discord.Member):
    """Says when a member joined."""
    yield from bot.say('{0.name} joined in {0.joined_at}'.format(member))

@bot.group(pass_context=True)
@asyncio.coroutine cool(ctx):
    """Says if a user is cool.

    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        yield from bot.say('No, {0.subcommand_passed} is not cool'.format(ctx))

@cool.command(name='bot')
@asyncio.coroutine _bot():
    """Is the bot cool?"""
    yield from bot.say('Yes, the bot is cool.')

def load_credentials():
    with open('credentials.json') as f:
        return json.load(f)

if __name == '__main__':
    credentials = load_credentials()
    bot.client_id = credentials['client_id']
    bot.bots_key = credentials['token']

    bot.run('token')

    handlers = log.handlers[:]
    for hdlr in handlers:
        hdlr.close()
        log.removeHandler(hdlr)
