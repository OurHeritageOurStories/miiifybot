from decouple import config
import logging

logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(
    filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter(
    '%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

class Context:
    pass

ctx = Context()

ctx.logger = logger

ctx.miiify_local_url = config('MIIIFY_LOCAL_URL')
ctx.miiify_remote_url = config('MIIIFY_REMOTE_URL')
ctx.container = config('CONTAINER')
ctx.username = config('GH_USERNAME')
ctx.password = config('GH_PASSWORD')
ctx.local_repo = config('LOCAL_REPO')
ctx.remote_repo = config('REMOTE_REPO')
ctx.upstream_repo = config('UPSTREAM_REPO')
ctx.repo_head = config('REPO_HEAD')
ctx.discord_token = config('DISCORD_TOKEN')
