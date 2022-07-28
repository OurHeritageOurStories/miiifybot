import discord
import logging
from decouple import config
from discord.ext import commands
from miiify import createAnnotation
from gh import pr as gh_pr
class Context:
    pass

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(
    filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter(
    '%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


client = discord.Client()
client = commands.Bot(command_prefix="!")


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    await client.process_commands(message)


@client.command()
async def square(ctx, arg):
    await ctx.send(int(arg) ** 2)


ctx = Context()
ctx.url = config('MIIIFY_URL')
ctx.gh_token = config('GH_TOKEN')

DISCORD_TOKEN = config('DISCORD_TOKEN')

gh_pr(ctx)

#print(createAnnotation(ctx, "hello world", "some page"))

#client.run(DISCORD_TOKEN)
