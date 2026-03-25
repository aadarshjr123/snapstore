import os 
import hashlib


REPO_DIR = ".snapstore"
OBJECTS_DIR = os.path.join(REPO_DIR,"objects")
def build_tree_recursive(path="."):
    entries = []

    for item in os.listdir(path):
        # Skip repo folder
        if item in [".snapstore", ".git", "__pycache__"]:
            continue

        full_path = os.path.join(path, item)

        # 🔹 FILE → BLOB
        if os.path.isfile(full_path):
            with open(full_path, "rb") as f:
                content = f.read()

            blob = b"blob\n" + content
            blob_hash = hashlib.sha1(blob).hexdigest()

            blob_path = os.path.join(OBJECTS_DIR, blob_hash)

            if not os.path.exists(blob_path):
                with open(blob_path, "wb") as f:
                    f.write(blob)

            entries.append(f"blob {blob_hash} {item}")

        # 🔹 DIRECTORY → TREE (recursive)
        elif os.path.isdir(full_path):
            tree_hash = build_tree_recursive(full_path)
            entries.append(f"tree {tree_hash} {item}")

    # Create tree object
    tree_content = "tree\n" + "\n".join(entries) + "\n"
    tree_bytes = tree_content.encode()

    tree_hash = hashlib.sha1(tree_bytes).hexdigest()
    tree_path = os.path.join(OBJECTS_DIR, tree_hash)

    if not os.path.exists(tree_path):
        with open(tree_path, "wb") as f:
            f.write(tree_bytes)

    return tree_hash



def restore_tree(tree_hash, base_path="."):

    tree_path = os.path.join(OBJECTS_DIR, tree_hash)

    with open(tree_path, "rb") as f:
        content = f.read().decode()

    lines = content.split("\n")[1:]  # skip "tree"

    for line in lines:
        if not line.strip():
            continue

        obj_type, obj_hash, name = line.split(" ")
        if name in [".snapstore",".git"]:
            continue

        full_path = os.path.join(base_path, name)

        if obj_type == "blob":
            blob_path = os.path.join(OBJECTS_DIR, obj_hash)

            with open(blob_path, "rb") as f:
                blob = f.read()

            file_content = blob.split(b"\n", 1)[1]

            with open(full_path, "wb") as out:
                out.write(file_content)

        elif obj_type == "tree":
            os.makedirs(full_path, exist_ok=True)
            restore_tree(obj_hash, full_path)
