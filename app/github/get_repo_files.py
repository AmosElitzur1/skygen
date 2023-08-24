import os
from git import Repo
import sys


def clean_path(destination_path):
    os.rmdir(destination_path)
    os.listdir(".")


def clone_repository(repo_url, destination_path):
    try:
        clean_path(destination_path)
        Repo.clone_from(repo_url, destination_path)
        print(f"Repository cloned to {destination_path}")
    except Exception as e:
        print("Error:", e)

repo_url = "https://github.com/AmosElitzur1/skygen.git"
destination_path = "cloned_repo"

clone_repository(repo_url, destination_path)


def build_file_tree(root_path):
    file_tree = {}
    for root, dirs, files in os.walk(root_path):
        # Skip directories that start with "."
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        current_dir = file_tree
        root_parts = os.path.relpath(root, root_path).split(os.path.sep)

        for part in root_parts:
            current_dir = current_dir.setdefault(part, {})

        for file in files:
            # Skip files that start with "."
            if not file.startswith('.'):
                current_dir[file] = None

    return file_tree

file_tree = build_file_tree("cloned_repo")
print(file_tree)