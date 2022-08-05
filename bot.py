from ast import AnnAssign
import discord
import logging
from decouple import config
from discord.ext import commands

from annotation import Annotation

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

    if message.content.startswith('$describe'):
        await message.channel.send(anno.describe(message.author.display_name, message.content))

    await client.process_commands(message)


@client.command()
async def square(ctx, arg):
    await ctx.send(int(arg) ** 2)


ctx = Context()
ctx.miiify_url = config('MIIIFY_URL')
ctx.username = config('USERNAME')
ctx.password = config('PASSWORD')
ctx.local_repo = config('LOCAL_REPO')
ctx.remote_repo = config('REMOTE_REPO')
ctx.upstream_repo = config('UPSTREAM_REPO')
ctx.repo_head = config('REPO_HEAD')

DISCORD_TOKEN = config('DISCORD_TOKEN')

anno = Annotation(ctx)

client.run(DISCORD_TOKEN)
