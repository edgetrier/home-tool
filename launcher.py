import streamlit as st
import sqlite3
import utils

# Config Streamlit Config
st.set_page_config(page_title="EdgeTrier Home Tool")

utils.page_init() # Initalisation

st.switch_page("pages/homepage.py")
