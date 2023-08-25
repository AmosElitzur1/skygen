import streamlit as st
from github.utils import parseTfvars, find_tfvars_files
from github.get_repo_files import clone_repository
from github.get_repos import search_public_repositories
from envs import get_envs
from generate import generate_all
import requests
from github.get_repo_files import clone_repository, build_file_tree
from prompts import generate_automation_prompt
from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings
import re
disable_warnings(InsecureRequestWarning) ## not needed, added by Adir

print("################ start ####################")
destination_path = "cloned_repo"

if 'stage' not in st.session_state:
    st.session_state.stage = "before_insert_git"

def click_submit_button(git_owner):
    st.session_state.stage = "after_git_owner_submit"
    st.session_state.git_owner = git_owner
    st.session_state.git_repos = search_public_repositories(git_owner)

def choose_repo(repo_name):
    if repo_name != "" and repo_name != "Choose repository":
        git_url = "https://github.com/"+st.session_state.git_owner+"/"+repo_name+".git"
        print(git_url)
        st.session_state.stage = "after_git_submit"
        st.session_state.repo_url = git_url

if st.session_state.stage == "before_insert_git":
    st.session_state.git_repos = []

git_owner = st.sidebar.text_input("Git Owner")
if "git_owner" not in st.session_state:
    st.session_state.git_owner = git_owner
st.sidebar.button("Submit Owner", on_click=click_submit_button, args=[git_owner])

# if st.session_state.stage == "after_git_owner_submit":
repo_name = st.sidebar.selectbox("Select repo", st.session_state.git_repos)
st.sidebar.button("Submit Repo", on_click=choose_repo, args=[repo_name])

if st.session_state.stage == "after_git_submit":
    repo_url = st.session_state.repo_url
    print(repo_url)
    clone_repository(repo_url, destination_path)
    st.session_state.stage = "after_clone"

def page_add():
    st.title("Add Env")
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

def page_manage():
    st.title("Edit Envs")
    if st.session_state.stage == "after_clone":
        tfvars_files = find_tfvars_files(destination_path)
        tfvars_files_names = [file_path.replace(destination_path, "") for file_path in tfvars_files]
        get_envs(tfvars_files_names, destination_path)

def page_ai_gen():
    tree = build_file_tree(destination_path)

    API_URL = "https://flowise-9ihn.onrender.com/api/v1/prediction/5e73c1f1-82a2-4c13-9d88-36d8878b34ca"
    payload = {
        "question": f"{generate_automation_prompt} {tree}",
    }  
    output = requests.post(API_URL, json=payload, verify=False).json()

    yaml_match = re.search(r'```yaml\n(.*?)```', output, re.DOTALL)
    if yaml_match:
        yaml_content = yaml_match.group(1)
        print(yaml_content)
    else:
        print("No YAML code block found.")

    code = f'''
    {yaml_content}
    '''
    st.code(code, language='python')

def main():
    st.sidebar.title("Navigation")
    pages = ["Add env", "Manage envs", "Workflow AI Generator"]
    choice = st.sidebar.radio("Go to", pages)

    if choice == "Add env":
        page_add()
    elif choice == "Manage envs":
        page_manage()
    elif choice == "Workflow AI Generator":
        page_ai_gen()

if __name__ == "__main__":
    main()