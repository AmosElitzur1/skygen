import os
import shutil


def create_workflow(source_file, target_root_directory):
    print(f"github/{source_file}")
    print(target_root_directory)
    print(os.getcwd())
    target_directory = f"{target_root_directory}/.github/workflows"
    if not os.path.exists(f"{target_directory}/skygen.yaml"):
        os.makedirs(target_directory)
    else:
        print(f"File '{target_directory}' not found.")
    shutil.copy(f"github/{source_file}", f"{target_directory}/skygen.yaml")
    print(f"File '{source_file}' copied to '{target_directory}/skygen.yaml'.")


