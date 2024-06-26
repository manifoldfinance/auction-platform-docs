#!/usr/bin/env python3

from pygit2 import Repository
import re

"""
GitHub branch/tag URL replacer
"""
# //github.com/M/platform-docs
regex = r"(github\.com/.+/MEV-Protocol/.+)/master/"
subst = "\\1/%s/"


def define_env(env):
    repo = Repository(".")
    if repo is not None:
        try:
            target = repo.head.shorthand
        except Exception:
            target = "master"
    else:
        target = "master"

    env.variables["current_branch"] = target


def on_post_page_macros(env):
    """
    Replace the branch/tag in the rook GitHub file and directory links pointing to `master`
    with the correct one that is currently active.
    """

    target = env.variables["current_branch"]
    if target == "master":
        return

    env.raw_markdown = re.sub(regex, subst % target, env.raw_markdown, 0)