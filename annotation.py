from miiify import Miiify
from gh import Repository
from manifest import Manifest


class Annotation:
    def __init__(self, ctx):
        self.miiify = Miiify(ctx)
        self.repo = Repository(ctx)
        self.logger = ctx.logger
        self.container = ctx.container
        self.manifest = Manifest(ctx)
        self.target_prefix = ctx.target_prefix

    def clone(self, ctx):
        repo = self.repo.clone(ctx)
        return f"{repo.description}\n cloned {ctx.remote_repo} to {ctx.local_repo}"

    def create_container(self, ctx):
        status_code = self.miiify.create_container("A Container for Miiifybot")
        if status_code == 201:
            self.repo.pull_request(
                "Miiifybot", f"create {ctx.container} container")
            return f"Annotation container {ctx.container} created"
        else:
            return f"Using annotation container {ctx.container}"

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

    def __make_localhost_annotation(self, uri):
        lis = uri.split('/')
        lis[2] = self.miiify.host(self.miiify.miiify_local_url)
        return '/'.join(lis)

    def redact(self, dict):
        self.logger.info(f"redact: {dict}")
        try:
            desc = dict['description']
            lis = desc.split('\n')
            complete = True
            for id in lis:
                if self.__is_annotation(id):
                    uri = id.strip()
                    local_uri = self.__make_localhost_annotation(uri)
                    self.__delete_annotation(local_uri)
                else:
                    complete = False
                    self.logger.info(
                        f"Ignoring {id} as it does not appear to be a valid annotation uri")
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
        target = self.target_prefix+lis[1]
        if self.manifest.target_exists(target):
            body = ' '.join(lis[2:])
            if body == '':
                return "Need to provide a description for the item"
            self.miiify.create_annotation(author, body, target)
            self.repo.pull_request("Miiifybot", f"discord user {author}")
            return f"{author} submitted an annotation for review"
        else:
            return f"{target} does not exist"

    def about(self, content):
        lis = content.split(' ')
        target = self.target_prefix+lis[1]
        if self.manifest.target_exists(target):
            res = self.miiify.read_annotation(target)
            return res
        else:
            return f"{target} does not exist"
