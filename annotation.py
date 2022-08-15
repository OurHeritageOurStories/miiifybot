from miiify import Miiify
from gh import Repository


class Annotation:
    def __init__(self, ctx):
        self.miiify = Miiify(ctx)
        self.repo = Repository(ctx)
        self.logger = ctx.logger
        self.container = ctx.container

    def clone(self, ctx):
        self.repo.clone(ctx)
        return f"cloned {ctx.remote_repo} to {ctx.local_repo}"

    def create_container(self, ctx):
        self.miiify.create_container("A Container for Miiifybot")
        self.repo.pull_request(
            "Miiifybot", f"create {ctx.container} container")
        return f"Container {ctx.container} created"

    def __delete_annotation(self, id):
        self.miiify.delete_annotation(id)
        self.repo.pull_request("Miiifybot", f"delete {id} annotation")
        return f"Annotation {id} deleted"

    def __is_annotation(self, uri):
        match uri.split('/'):
            case [proto, '', host, 'annotations', self.container, annotation]:
                return True
            case _ as uri:
                return False

    def redact(self, dict):
        try:
            desc = dict['description']
            lis = desc.split('\n')
            complete = True
            for id in lis:
                if self.__is_annotation(id):
                    self.__delete_annotation(id.strip())
                else:
                    complete = False
                    self.logger.info(f"Ignoring {id} as it does not appear to be a valid annotation uri")
        except:
            self.logger.error('was not able to parse the embeds content')
            return "burp!"
        else:
            if complete == True:
                self.logger.info('redacted all the annotations supplied')
                return "redacted content"
            else:
                self.logger.error('did not redact all the annotations')
                return "burp!"

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
