import os

def generate_tfvars(full_path, input_tfvars, new_tfvars_file_name) -> str:
    new_path = os.path.dirname(full_path) + "/" + new_tfvars_file_name
    lines = []
    for key in input_tfvars.keys():
        lines.append(f"{key} = \"{input_tfvars[key]}\"")
    str_lines = "\n".join(lines)
    with open(new_path, "w") as f:
        f.write(str_lines)
    return str_lines, new_path