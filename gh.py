from github import Github
from git import Repo


class Repository:
    def __init__(self, ctx):
        self.local_repo = ctx.local_repo
        self.remote_repo = ctx.remote_repo
        self.upstream_repo = ctx.upstream_repo
        self.username = ctx.username
        self.password = ctx.password
        self.repo_head = ctx.repo_head

    def clone(self, ctx):
        remote = f"https://{self.username}:{self.password}@github.com/{self.remote_repo}.git"
        Repo.clone_from(remote, self.local_repo)

    def __push(self):
        repo = Repo(self.local_repo)
        origin = repo.remote(name="origin")
        origin.push()

    def __pr(self, title, body):
        g = Github(self.password)
        repo = g.get_repo(self.upstream_repo)
        # this could be more robust
        pulls = repo.get_pulls(state='open')
        users = list(map(lambda x: x.user.login, pulls))
        if self.username in users:
            return
        else:
            pr = repo.create_pull(title, body, base="master",
                              head=self.repo_head)

    def pull_request(self, title, body):
        self.__push()
        self.__pr(title, body)
