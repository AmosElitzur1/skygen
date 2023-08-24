import os
import shutil


def create_workflow(source_file, target_root_directory):
    print(f"github/{source_file}")
    print(target_root_directory)
    print(os.getcwd())
    target_directory = f"{target_root_directory}/.github/workflows"
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)
        shutil.copy(f"github/{source_file}", f"{target_directory}/skygen.yaml")
        print(f"File '{source_file}' copied to '{target_directory}/skygen.yaml'.")
    else:
        print(f"File '{target_directory}' not found.")



