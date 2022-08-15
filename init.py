from os.path import exists
import subprocess
import time

class Init:
    def __init__(self, ctx, anno):
        if exists(ctx.local_repo):
            pass
        else:
            print(anno.clone(ctx))
            res = subprocess.run(["./miiify.sh"])
            print(res)
            time.sleep(2.0) # need to wait for container
            res = anno.create_container(ctx)
            print(res)



    