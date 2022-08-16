from os.path import exists
import subprocess
import time

class Init:

    def __init__(self, ctx, anno):
        self.miiify_local_url = ctx.miiify_local_url
        if exists(ctx.local_repo):
            pass
        else:
            print(anno.clone(ctx))
            subprocess.run(["./miiify.sh"])
            while anno.miiify.is_alive() == False:
                print("Waiting for miiify to come alive")
                time.sleep(2.0)
            print(anno.create_container(ctx))



    