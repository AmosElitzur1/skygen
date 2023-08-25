import streamlit as st
from github.create_workflow import create_workflow
from github.get_repo_files import push_to_github
from file_utils import generate_tfvars

destination_path = "cloned_repo"

def generate_all(selected_file, input_tfvars, new_tfvars_file_name):
    print(selected_file, input_tfvars)
    new_tfvars, full_file_path = generate_tfvars(selected_file, input_tfvars, new_tfvars_file_name)
    create_workflow("workflow_template.yaml", destination_path)
    st.header("New tfvars")
    push_to_github(destination_path, full_file_path.replace(f"{destination_path}/", ""))
    st.code(new_tfvars, language="hcl", line_numbers=True)
    st.session_state.stage = "generate_pressed"