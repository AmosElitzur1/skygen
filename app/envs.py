import streamlit as st
import numpy as np

def get_envs(envs_list):
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
            button_col1, button_col2, button_col3 = col.columns(3)
            if button_col1.button("✅", "apply_"+item):
                st.write(f"Button 1 clicked for {item}")
            if button_col2.button("🖋️", "edit_"+item):
                st.write(f"Button 2 clicked for {item}")
            if button_col3.button("🗑️", "destroy_"+item):
                st.write(f"Button 2 clicked for {item}")

            with col:
                col.markdown("---")
