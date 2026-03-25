import os

REPO_DIR = ".snapstore"
HEAD_FILE = os.path.join(REPO_DIR, "HEAD")

def get_current_branch():
    with open(HEAD_FILE, "r") as f:
        ref = f.read().strip()
    return ref.replace("ref: ", "")

def get_head_commit():
    branch_path = os.path.join(REPO_DIR, get_current_branch())

    if not os.path.exists(branch_path):
        return ""

    with open(branch_path, "r") as f:
        return f.read().strip()

def update_head(commit_hash):
    branch_path = os.path.join(REPO_DIR, get_current_branch())

    with open(branch_path, "w") as f:
        f.write(commit_hash)