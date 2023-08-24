import streamlit as st
import pandas as pd
 
st.write("""
# SKYGEN TEAM!!!!
We Are The *Champions!*
""")
 
df = pd.read_csv("my_data.csv")
st.line_chart(df)

st.button("amos")