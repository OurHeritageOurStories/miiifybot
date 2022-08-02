from miiify import Miiify
from gh import Repository

class Annotation:
    def __init__(self, ctx):
        self.miiify = Miiify(ctx)
        self.repo = Repository(ctx)


    def describe(self):
        self.miiify.create_annotation("foo", "bar")
        self.repo.pull_request("baz", "boz")
        return "test complete"
    
