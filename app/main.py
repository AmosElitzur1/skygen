import streamlit as st
from github.utils import parseTfvars, find_tfvars_files
from github.get_repo_files import clone_repository

# tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

# with tab1:
#     st.header("A cat")
#     st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

# with tab2:
#     st.header("A dog")
#     st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

# with tab3:
#     st.header("An owl")
#     st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

repo_url = st.text_input("Git URL")

def click_submit_button():
    st.session_state.submit_button_clicked = True

def generate_all(selected_file, input_tfvars):
    st.session_state.generate_all_clicked = True
    print(selected_tfvars_file, input_tfvars)


if 'submit_button_clicked' not in st.session_state:
    st.session_state.submit_button_clicked = False
st.button("Submit", on_click=click_submit_button)
if st.session_state.submit_button_clicked:
    print(repo_url)
    destination_path = "cloned_repo"
    clone_repository(repo_url, destination_path)
    tfvars_files = find_tfvars_files(destination_path)
    tfvars_files_names = [file_path.replace(destination_path, "") for file_path in tfvars_files]
    selected_tfvars_file = st.selectbox("Select tfvars file", tfvars_files_names)
    selected_tfvars_file_full_path = f"{destination_path}{selected_tfvars_file}"
    parsedTfvars = parseTfvars(selected_tfvars_file_full_path)
    input_tfvars = {}
    for key in parsedTfvars.keys():
        input_tfvars[key] = st.text_input(label=key, value=parsedTfvars[key])
    st.button("Generate the SKY🌇", on_click=generate_all, args=[selected_tfvars_file_full_path, input_tfvars])
