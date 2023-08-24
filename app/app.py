import streamlit as st
import pandas as pd
import datetime
 
st.write("""
# SKYGEN TEAM!!!!
We Are The *Champions!*
""")
 
st.write(f'<h2>{datetime.datetime.now()}<h2>', unsafe_allow_html=True)
df = pd.read_csv("my_data.csv")
st.line_chart(df)

st.button("amos")