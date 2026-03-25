import os 
import hashlib
import time
from snapstore.storage.refs import get_head_commit, update_head
from snapstore.core.tree import build_tree_recursive

REPO_DIR = ".snapstore"
OBJECTS_DIR = os.path.join(REPO_DIR,"objects")
HEAD_FILE = os.path.join(REPO_DIR,"HEAD")

def commit(message):
    
    parent = get_head_commit()
    tree_hash = build_tree_recursive(".")

    # 🔥 Detect no changes
    if parent:
        parent_path = os.path.join(OBJECTS_DIR, parent)

        with open(parent_path, "rb") as f:
            parent_content = f.read().decode()

        for line in parent_content.split("\n"):
            if line.startswith("tree:"):
                old_tree = line.replace("tree: ", "").strip()

                if old_tree == tree_hash:
                    print("Nothing to commit.")
                    return

    commit_content = f"commit\n"
    commit_content += f"tree: {tree_hash}\n"
    commit_content += f"parent: {parent}\n"
    commit_content += f"timestamp: {int(time.time())}\n\n"
    commit_content += f"{message}\n"

    commit_bytes = commit_content.encode()
    commit_hash = hashlib.sha1(commit_bytes).hexdigest()

    object_path = os.path.join(OBJECTS_DIR, commit_hash)

    with open(object_path, "wb") as f:
        f.write(commit_bytes)

    update_head(commit_hash)

    print(f"Committed as {commit_hash}")


def log():
    if not os.path.exists(HEAD_FILE):
        print("No commits yet.")
        return

    commit_hash = get_head_commit()

    while commit_hash:
        object_path = os.path.join(OBJECTS_DIR, commit_hash)

        if not os.path.exists(object_path):
            break

        with open(object_path, "rb") as f:
            content = f.read().decode()

        lines = content.split("\n")

        parent = ""
        message = ""

        for i, line in enumerate(lines):
            if line.startswith("parent:"):
                parent = line.replace("parent: ", "").strip()

            # message starts after empty line
            if line.strip() == "" and i + 1 < len(lines):
                message = lines[i + 1]
                break

        print("Commit:", commit_hash)
        print("Message:", message)
        print("-" * 40)

        commit_hash = parent

    