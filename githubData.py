from pygit2 import Repository
from time import time
import sys

WEEK = 604800  # Number of seconds in a week


def getData(directory):
    repo = Repository(directory)
    branch = repo.head.shorthand
    deltas = repo.diff().deltas
    localChanges = False
    if next(deltas, None) is not None:
        localChanges = True
    lastCommit = str(repo.head.target)
    commitTime = repo.revparse_single(lastCommit).commit_time
    currentCommitThisWeek = False
    if time() - commitTime < 604800:
        currentCommitThisWeek = True
    isRufus = repo.revparse_single(lastCommit).author.name.lower() == 'rufus'
    print("active branch: " + branch)
    print("local changes: " + str(localChanges))
    print("recent commit: " + str(currentCommitThisWeek))
    print("blame Rufus: " + str(isRufus))


if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    getData(sys.argv[1])
