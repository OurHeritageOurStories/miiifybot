from github import Github


def pr(ctx):
    g = Github(ctx.gh_token)
    # test printing repos for now
    for repo in g.get_user().get_repos():
        print(repo.name)