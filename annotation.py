from miiify import Miiify
from gh import Repository

class Annotation:
    def __init__(self, ctx):
        self.miiify = Miiify(ctx)
        self.repo = Repository(ctx)


    def describe(self, author, content):
        lis = content.split(' ')
        target = lis[1]
        body = ' '.join(lis[2:])
        self.miiify.create_annotation(body, target)
        self.repo.pull_request("Miiifybot", f"discord user {author}")
        return f"annotation submiited for review by {author}"


    def about(self, content):
        lis = content.split(' ')
        item = lis[1]
        res = self.miiify.read_annotation(item)
        return res

    
