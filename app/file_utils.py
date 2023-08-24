def generate_tfvars(input_tfvars) -> str:
    lines = []
    for key in input_tfvars.keys():
        lines.append(f"{key} = {input_tfvars[key]}")
    str_lines = "\n".join(lines)
    return str_lines