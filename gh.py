from github import Github
from git import Repo

def clone(ctx):
    full_local_path = "db"
    username = "testjohny"
    password = ctx.gh_token
    remote = f"https://{username}:{password}@github.com/testjohny/annotations.git"
    Repo.clone_from(remote, full_local_path)


def push(ctx):
    repo = Repo("db")
    origin = repo.remote(name="origin")
    origin.push()


def pr(ctx, title, body):
    g = Github(ctx.gh_token)
    repo = g.get_repo("jptmoore/annotations")
    pr = repo.create_pull(title, body, base="master", head="testjohny:master")
