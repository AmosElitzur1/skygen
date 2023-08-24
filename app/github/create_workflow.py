import os
import shutil


def create_workflow(source_file, target_root_directory):
    target_directory = f"{target_root_directory}/.github/workflows"
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)
        shutil.copy(source_file, f"{target_directory}/skygen.yaml")
        print(f"File '{source_file}' copied to '{target_directory}/skygen.yaml'.")
    else:
        print(f"File '{target_directory}' not found.")



