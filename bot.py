import discord
from annotation import Annotation
from context import ctx
from init import bootstrap

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    ctx.logger.info('Logged in as {0.user}'.format(client))


def handle_command(message):
    match message.content.split(' '):
        case ['$describe', item, *xs] if xs != []:
            author = message.author.display_name
            description = ' '.join(xs)
            item = item.lower()
            return anno.describe(author, item, description)
        case ['$about' | '$info', item]:
            item = item.lower()
            return anno.about(item)
        case ['$ping']:
            return 'pong'
        case ['$help']:
            return 'Commands available:\nabout <item>\ndescribe <item> <description>\nping'
        case _:
            return 'sorry I did not understand that'


@client.event
async def on_message(message):
    for embed in message.embeds:
        dict = embed.to_dict()
        await message.channel.send(anno.redact(dict))
    if message.author == client.user:
        return
    if message.content.startswith('$'):
        await message.channel.send(handle_command(message))


anno = Annotation(ctx)
bootstrap(ctx, anno)
client.run(ctx.discord_token)
