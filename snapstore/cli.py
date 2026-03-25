import sys

from snapstore.core.init import init
from snapstore.core.commit import commit, log
from snapstore.core.checkout import checkout
from snapstore.core.branch import branch, checkout_branch

def main():
    command = sys.argv[1]

    if command == "init":
        init()

    elif command == "commit":
        if sys.argv[2] == "-m":
            commit(sys.argv[3])

    elif command == "checkout":
        checkout(sys.argv[2])

    elif command == "log":
        log()

    elif command == "branch":
        branch(sys.argv[2])

    elif command == "checkout-branch":
        checkout_branch(sys.argv[2])