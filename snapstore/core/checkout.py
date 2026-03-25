import os 

from snapstore.utils.filesystem import clean_working_dir
from snapstore.core.tree import restore_tree
from snapstore.storage.refs import update_head


REPO_DIR = ".snapstore"
OBJECTS_DIR = os.path.join(REPO_DIR,"objects")
INDEX_FILE = os.path.join(REPO_DIR,"index")

def checkout(commit_hash):
    # Safety check
    if os.path.exists(INDEX_FILE):
        with open(INDEX_FILE, "r") as f:
            if f.read().strip():
                print("You have staged changes. Commit first.")
                return

    object_path = os.path.join(OBJECTS_DIR, commit_hash)

    if not os.path.exists(object_path):
        print("Commit not found.")
        return

    # Read commit
    with open(object_path, "rb") as f:
        content = f.read().decode()

    lines = content.split("\n")

    # Extract tree hash
    tree_hash = ""
    for line in lines:
        if line.startswith("tree:"):
            tree_hash = line.replace("tree: ", "").strip()

    if not tree_hash:
        print("Invalid commit (no tree found).")
        return

    clean_working_dir()
    # 🔥 Restore recursively
    restore_tree(tree_hash)

    update_head(commit_hash)

    print(f"Checked out {commit_hash}")


def restore_tree_from_commit(commit_hash):
    object_path = os.path.join(OBJECTS_DIR,commit_hash)
    
    with open(object_path,"rb") as f:
        content = f.read().decode()
    
    for line in content.split("\n"):
        if line.startswith("tree:"):
            tree_hash = line.replace("tree: ","").strip()
    
    clean_working_dir()
    restore_tree(tree_hash)
    
