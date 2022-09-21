import discord
from discord.ext import commands
from annotation import Annotation
from context import ctx
from init import Init

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

client = commands.Bot(command_prefix=".", intents=intents)


@client.event
async def on_ready():
    ctx.logger.info('We have logged in as {0.user}'.format(client))


def handle_command(message):
    match message.content.split(' '):
        case ['$describe', item, *xs]:
            author = message.author.display_name
            description = ' '.join(xs)
            return anno.describe(author, item, description)
        case ['$about', item]:
            return anno.about(item)
        case ['$ping']:
            return 'pong'
        case ['$help']:
            return 'Commands available:\nabout <item>\ndescribe <item> <description>\nping'
        case _:
            return 'sorry I did not understand that'


@client.event
async def on_message(message):

    embeds = message.embeds
    for embed in embeds:
        dict = embed.to_dict()
        await message.channel.send(anno.redact(dict))

    if message.author == client.user:
        return

    if message.content.startswith('$'):
        await message.channel.send(handle_command(message))

    await client.process_commands(message)


@client.command()
async def square(self, arg):
    await self.send(int(arg) ** 2)

anno = Annotation(ctx)

Init(ctx, anno)

client.run(ctx.discord_token)
