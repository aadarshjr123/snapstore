import os

REPO_DIR = ".snapstore"
OBJECTS_DIR = os.path.join(REPO_DIR, "objects")

def write_object(obj_hash, data):
    path = os.path.join(OBJECTS_DIR, obj_hash)

    if not os.path.exists(path):
        with open(path, "wb") as f:
            f.write(data)

def read_object(obj_hash):
    path = os.path.join(OBJECTS_DIR, obj_hash)

    if not os.path.exists(path):
        return None

    with open(path, "rb") as f:
        return f.read()