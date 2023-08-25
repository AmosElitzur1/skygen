import streamlit as st
import numpy as np
from github.utils import parseTfvars
from github.get_repo_files import *
from github.create_workflow import create_workflow
from generate import generate_all

destination_path = "cloned_repo"

def terraform_command_send(tf_command, cloned_repo_path, tfvars_path):
    create_workflow("workflow_template.yaml", cloned_repo_path)
    push_apply_to_github(cloned_repo_path, tfvars_path, tf_command)

def open_edit_page(selected_tfvars_file):
    selected_tfvars_file_full_path = f"{destination_path}{selected_tfvars_file}"
    parsedTfvars = parseTfvars(selected_tfvars_file_full_path)
    input_tfvars = {}
    for key in parsedTfvars.keys():
        input_tfvars[key] = st.text_input(label=key, value=parsedTfvars[key])
    st.button("Re-Generate the SKY🌇", on_click=generate_all, args=[selected_tfvars_file_full_path, input_tfvars, selected_tfvars_file_full_path])

def get_envs(envs_list, dest_path):
    num_items = len(envs_list)
    num_columns = 3
    num_rows = -(-num_items // num_columns)  # Ceiling division to calculate the number of rows

    for row in range(num_rows):
        col1, col2, col3 = st.columns(3)

        # Calculate the indices for the current row
        start_index = row * num_columns
        end_index = min(start_index + num_columns, num_items)

        # Display items and buttons in the current row
        for i in range(start_index, end_index):
            item = envs_list[i]
            item_short_name = item.split("/")[-1].replace(".tfvars","")
            col = col1 if i % 3 == 0 else col2 if i % 3 == 1 else col3

            with col:
                col.write(item_short_name)
                col.caption(item)

            # Add buttons
            button_col1, button_col2, button_col3, button_col4 = col.columns(4)
            button_col1.button("✅", "apply_"+item, on_click=terraform_command_send, args=["apply", dest_path, item])
            button_col2.button("️🛑", "destroy_"+item, on_click=terraform_command_send, args=["destroy", dest_path, item])
            button_col3.button("🖋️", "edit_"+item)
            button_col4.button("🗑️", "delete_"+item, on_click=terraform_command_send, args=["remove", dest_path, item])

            with col:
                col.markdown("---")
