import streamlit as st
from github.utils import parseTfvars, find_tfvars_files
from github.get_repo_files import clone_repository, push_to_github
from github.create_workflow import create_workflow
from file_utils import generate_tfvars

print("################ start ####################")

def click_submit_button(git_url):
    st.session_state.stage = "after_git_submit"
    st.session_state.repo_url = git_url


def generate_all(selected_file, input_tfvars, new_tfvars_file_name):
    print(selected_file, input_tfvars)
    # create_workflow(selected_file)
    new_tfvars = generate_tfvars(selected_file, input_tfvars, new_tfvars_file_name)
    st.header("New tfvars")
    push_to_github(destination_path)
    st.code(new_tfvars, language="hcl", line_numbers=True)
    st.session_state.stage = "generate_pressed"

destination_path = "cloned_repo"

with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )
if 'repo_url' in st.session_state:
    st.write(f"repo url: {st.session_state.repo_url}")

if 'stage' not in st.session_state:
    st.session_state.stage = "before_insert_git"

if st.session_state.stage == "before_insert_git":
    repo_url = st.text_input("Git URL")
    if "repo_url" not in st.session_state:
        st.session_state.repo_url = repo_url
    st.button("Submit", on_click=click_submit_button, args=[repo_url])

if st.session_state.stage == "after_git_submit":
    repo_url = st.session_state.repo_url
    print(repo_url)
    clone_repository(repo_url, destination_path)
    st.session_state.stage = "after_clone"

if st.session_state.stage == "after_clone":
    tfvars_files = find_tfvars_files(destination_path)
    tfvars_files_names = [file_path.replace(destination_path, "") for file_path in tfvars_files]
    selected_tfvars_file = st.selectbox("Select tfvars file", tfvars_files_names)
    selected_tfvars_file_full_path = f"{destination_path}{selected_tfvars_file}"
    parsedTfvars = parseTfvars(selected_tfvars_file_full_path)
    input_tfvars = {}
    new_tfvars_file_name = st.text_input(label="New Tfvars Filename")
    for key in parsedTfvars.keys():
        input_tfvars[key] = st.text_input(label=key, value=parsedTfvars[key])
    st.button("Generate the SKY🌇", on_click=generate_all, args=[selected_tfvars_file_full_path, input_tfvars, new_tfvars_file_name])

if st.session_state.stage == "generate_pressed":
    st.write("this will be the workflow and the new tf vars")