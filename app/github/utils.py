import os


def find_tfvars_files(directory) -> dict:
    # List to store the file paths
    tfvars_files = {}

    # Walk through directory
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith('.tfvars'):
                tfvars_files[filename] = os.path.join(dirpath, filename)
    return tfvars_files

def parseTfvars(tfVarsFile: str) -> dict:
    tfVars = {}
    with open(tfVarsFile, 'r') as f:
        for line in f.readlines():
            if line.startswith('#') or line.startswith('\n'):
                continue
            else:
                key, value = line.split('=')
                tfVars[key.strip()] = value.replace('"', '')
    return tfVars
