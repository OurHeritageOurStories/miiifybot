from decouple import config

class Context:
    pass

ctx = Context()
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
