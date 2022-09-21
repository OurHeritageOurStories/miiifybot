from os.path import exists
import subprocess
import time


def bootstrap(ctx, anno):
    if exists(ctx.local_repo):
        pass
    else:
        print(anno.clone(ctx))
        subprocess.run(["./miiify.sh"])
        while anno.miiify.is_alive() == False:
            print("Waiting for miiify to come alive")
            time.sleep(2.0)
        print(anno.create_container(ctx))
