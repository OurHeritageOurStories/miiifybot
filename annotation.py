from miiify import Miiify
from gh import Repository

class Annotation:
    def __init__(self, ctx):
        self.miiify = Miiify(ctx)
        self.repo = Repository(ctx)

    def clone(self, ctx):
        self.repo.clone(ctx)
        return f"cloned {ctx.remote_repo} to {ctx.local_repo}"


    def create_container(self, ctx):
        self.miiify.create_container("A Container for Miiifybot")
        self.repo.pull_request("Miiifybot", f"create {ctx.container} container")
        return f"Container {ctx.container} created"

    def __delete_annotation(self, id):
        self.miiify.delete_annotation(id)
        self.repo.pull_request("Miiifybot", f"delete {id} annotation")
        return f"Annotation {id} deleted"


    def redact(self, dict):
        desc = dict['description']
        lis = desc.split('\n')
        for id in lis:
            self.__delete_annotation(id.strip())
        return "redacted content"


    def describe(self, author, content):
        lis = content.split(' ')
        target = lis[1]
        body = ' '.join(lis[2:])
        self.miiify.create_annotation(author, body, target)
        self.repo.pull_request("Miiifybot", f"discord user {author}")
        return f"{author} submitted an annotation for review"


    def about(self, content):
        lis = content.split(' ')
        item = lis[1]
        res = self.miiify.read_annotation(item)
        return res

    
