"""
This file contains all utility functions
author:Clifford
"""

import sqlite3
import streamlit as st
import os

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
    Initalisation function when loading each pages
    """
    st.set_page_config(
        page_title="EdgeTrier Home Tool",
        initial_sidebar_state="collapsed",
        layout="wide",
        menu_items={
            "About": """
                    ### EdgeTrier Home Tool

                    **Version 0.1**

                    Author: Clifford Zhang

                    Website: [https://edgetrier.one](edgetrier.one)

                    Github Repo: [https://github.com/edgetrier/home-tool](github.com/edgetrier/home-tool)
                    """
        }
    )

    load_db() # Load Database


    