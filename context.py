from decouple import config as config_env
from configparser import ConfigParser
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
config_ini = ConfigParser()
config_ini.read('config.ini')

# config.ini settings
ctx.miiify_local_url = config_ini.get('main', 'MIIIFY_LOCAL_URL')
ctx.miiify_remote_url = config_ini.get('main', 'MIIIFY_REMOTE_URL')
ctx.manifest_url = config_ini.get('main', 'MANIFEST_URL')
ctx.target_prefix = config_ini.get('main', 'TARGET_PREFIX')
ctx.container = config_ini.get('main', 'CONTAINER')
ctx.local_repo = config_ini.get('main', 'LOCAL_REPO')
ctx.remote_repo = config_ini.get('main', 'REMOTE_REPO')
ctx.upstream_repo = config_ini.get('main', 'UPSTREAM_REPO')
ctx.repo_head = config_ini.get('main', 'REPO_HEAD')

# .env settings
ctx.discord_token = config_env('DISCORD_TOKEN')
ctx.username = config_env('GH_USERNAME')
ctx.password = config_env('GH_PASSWORD')