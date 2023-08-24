import streamlit as st
import os

st.text_input("Git URL")


def find_tfvars_files(directory):
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

def click_submit_button():
    st.session_state.submit_button_clicked = True


if 'submit_button_clicked' not in st.session_state:
    st.session_state.submit_button_clicked = False
st.button("Submit", on_click=click_submit_button)
if st.session_state.submit_button_clicked:
    parsedTfvars = parseTfvars("demo.tfvars")
    for key in parsedTfvars.keys():
        st.text_input(label=key, value=parsedTfvars[key])
