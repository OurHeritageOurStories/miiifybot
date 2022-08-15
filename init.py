from os.path import exists
import subprocess


class Init:
    def __init__(self, ctx, anno):
        if exists(ctx.local_repo):
            pass
        else:
            print(anno.clone(ctx))
            subprocess.run(["./miiify.sh"])

    