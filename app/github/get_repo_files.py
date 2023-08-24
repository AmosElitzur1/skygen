import os
from git import Repo
import sys
import shutil


def clean_path(directory_path):
    try:
        shutil.rmtree(directory_path)
        print(f"Directory '{directory_path}' removed successfully.")
    except Exception as e:
        print(f"Error removing directory '{directory_path}': {e}")


def clone_repository(repo_url, destination_path):
    try:
        clean_path(destination_path)
        Repo.clone_from(repo_url, destination_path)
        print(f"Repository cloned to {destination_path}")
    except Exception as e:
        print("Error:", e)


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
            if not file.startswith('.'):
                current_dir[file] = None

    return file_tree


def push_to_github(cloned_repo_path):
    repo = Repo(cloned_repo_path)
    repo.git.add('--all')
    # Commit
    staged_files = [item.a_path for item in repo.index.diff(None)]
    commit_message = f"The following files were updated: {', '.join(staged_files)}"
    repo.index.commit(commit_message)
    # Assuming you have a remote named "origin"
    repo.remotes.origin.push()

    

if __name__ == '__main__':
    repo_url = "https://github.com/AmosElitzur1/skygen.git"
    destination_path = "cloned_repo"
    if len(sys.argv) >= 2:
        repo_url = sys.argv[1]
    if len(sys.argv) == 3:
        destination_path = sys.argv[2]
    clone_repository(repo_url, destination_path)
    file_tree = build_file_tree(destination_path)
    print(file_tree)