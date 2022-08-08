import discord
import logging
from discord.ext import commands

from annotation import Annotation
from context import ctx

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

    if message.content.startswith('$about'):
        await message.channel.send(anno.about(message.content))
       

    await client.process_commands(message)


@client.command()
async def square(self, arg):
    await self.send(int(arg) ** 2)

@client.command()
async def clone(self):
    await self.send(anno.clone(ctx))


anno = Annotation(ctx)

client.run(ctx.discord_token)
