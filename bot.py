import discord
from discord.ext import commands
from annotation import Annotation
from context import ctx
from init import Init

client = discord.Client()
client = commands.Bot(command_prefix=".")

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):

    embeds = message.embeds
    for embed in embeds:
        dict = embed.to_dict()
        await message.channel.send(anno.redact(dict))

    if message.author == client.user:
        return

    if message.content.startswith('$ping'):
        await message.channel.send("**pong**")

    if message.content.startswith('$describe'):
        await message.channel.send(anno.describe(message.author.display_name, message.content))

    if message.content.startswith('$about'):
        await message.channel.send(anno.about(message.content))
       

    await client.process_commands(message)


@client.command()
async def square(self, arg):
    await self.send(int(arg) ** 2)

anno = Annotation(ctx)

Init(ctx, anno)

client.run(ctx.discord_token)
