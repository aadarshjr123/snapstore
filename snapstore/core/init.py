import os

REPO_DIR = ".snapstore"

def init():
    if os.path.exists(REPO_DIR):
        print("Repo already exist.")
        return
    
    os.makedirs(os.path.join(REPO_DIR, "objects"))
    os.makedirs(os.path.join(REPO_DIR, "refs", "heads"))

    with open(os.path.join(REPO_DIR, "refs", "heads", "main"), "w"):
        pass

    with open(os.path.join(REPO_DIR, "HEAD"), "w") as f:
        f.write("ref: refs/heads/main")

    print("Initialized empty snapstore repo.")