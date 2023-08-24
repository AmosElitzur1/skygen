import streamlit as st
from github.utils import parseTfvars, find_tfvars_files
from github.get_repo_files import clone_repository, push_to_github
from github.create_workflow import create_workflow
from github.get_repos import search_public_repositories
from file_utils import generate_tfvars

print("################ start ####################")
destination_path = "cloned_repo"

def click_submit_button(git_owner):
    st.session_state.stage = "after_git_owner_submit"
    st.session_state.git_owner = git_owner
    st.session_state.git_repos = search_public_repositories(git_owner)

def choose_repo(git_url):
    print(git_url)
    if git_url != "":
        st.session_state.stage = "after_git_submit"
        st.session_state.repo_url = git_url

def generate_all(selected_file, input_tfvars, new_tfvars_file_name):
    print(selected_file, input_tfvars)
    new_tfvars = generate_tfvars(selected_file, input_tfvars, new_tfvars_file_name)
    create_workflow("workflow_template.yaml", destination_path)
    st.header("New tfvars")
    push_to_github(destination_path)
    st.code(new_tfvars, language="hcl", line_numbers=True)
    st.session_state.stage = "generate_pressed"


if 'stage' not in st.session_state:
    st.session_state.stage = "before_insert_git"

if st.session_state.stage == "before_insert_git":
    st.session_state.git_repos = []

git_owner = st.text_input("Git Owner")
if "git_owner" not in st.session_state:
    st.session_state.git_owner = git_owner
st.button("Submit Owner", on_click=click_submit_button, args=[git_owner])

# if st.session_state.stage == "after_git_owner_submit":
repo_url = st.selectbox("Select repo", st.session_state.git_repos)
st.button("Submit Repo", on_click=choose_repo, args=[repo_url])

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