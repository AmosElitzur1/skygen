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


if 'submit_button_clicked' not in st.session_state:
    st.session_state.submit_button_clicked = False
st.button("Submit", on_click=click_submit_button)
if st.session_state.submit_button_clicked:
    print(repo_url)
    destination_path = "cloned_repo"
    clone_repository(repo_url, destination_path)
    tfvars_files = find_tfvars_files(destination_path)
    for tfvarfile in tfvars_files.keys():
        parsedTfvars = parseTfvars(tfvars_files[tfvarfile])
        for key in parsedTfvars.keys():
            st.text_input(label=key, value=parsedTfvars[key])
