
import os 

from snapstore.storage.refs import get_head_commit
from snapstore.utils.filesystem import clean_working_dir
from snapstore.core.checkout import restore_tree_from_commit




REPO_DIR = ".snapstore"
HEAD_FILE = os.path.join(REPO_DIR,"HEAD")

def branch(name):
    branch_path = os.path.join(REPO_DIR,"refs", "heads", name)
    if os.path.exists(branch_path):
        print("Branch already exists.")
        return
    
    head_commit = get_head_commit()

    with open(branch_path,"w") as f:
        f.write(head_commit)

    print(f"Branch '{name}' created.")


def checkout_branch(name):
    branch_path = os.path.join(REPO_DIR, "refs", "heads", name)

    if not os.path.exists(branch_path):
        print("Branch not found.")
        return
    
    with open(branch_path,"r") as f:
        commit_hash = f.read().strip()

    with open(HEAD_FILE,"w") as f:
        f.write(f"ref: refs/heads/{name}")

    if commit_hash:
        clean_working_dir()
        restore_tree_from_commit(commit_hash)

    print(f"Switched to branch '{name}'")

