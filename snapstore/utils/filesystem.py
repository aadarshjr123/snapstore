import os
import shutil

def clean_working_dir(base_path="."):
    for item in os.listdir(base_path):
        if item in [".snapstore", ".git", "__pycache__"]:
            continue
        
        full_path = os.path.join(base_path, item)

        if os.path.isfile(full_path):
            os.remove(full_path)

        elif os.path.isdir(full_path):
            shutil.rmtree(full_path)