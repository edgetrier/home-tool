"""
This file contains all utility functions
author:Clifford
"""

import sqlite3
import streamlit as st

def load_db():
    """
    Load database into streamlit state session
    """
    # Load Database
    db = sqlite3.connect("resources/database.db")
    db_cur = db.cursor()

    if "db" not in st.session_state:
        st.session_state["db"] = db
    if "db_cur" not in st.session_state:
        st.session_state["db_cur"] = db_cur

def page_init():
    """
    Initalisation function when loading each page
    """
    load_db()