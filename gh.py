from github import Github


def pr(ctx):
    g = Github(ctx.gh_token)
    repo = g.get_repo("jptmoore/annotations")
    pr = repo.create_pull(title="Miiifybot", body="automated test", base="master", head="testjohny:master")
