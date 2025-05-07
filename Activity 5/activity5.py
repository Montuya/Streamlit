# -*- coding: utf-8 -*-
"""
Created on Sun May  4 15:32:14 2025
@author: Administrator
"""

import streamlit as st
import streamlit_authenticator as stauth
import pandas as pd
from sqlalchemy import create_engine, text
import yaml
from yaml.loader import SafeLoader

# ----------------- CONFIG ------------------


# Database credentials
DB_USER = "root"
DB_PASS = ""
DB_HOST = "localhost"
DB_NAME = "streamlit"
TABLE_NAME = "mytable"

# User config (mimics config.yaml)
config = {
    'credentials': {
        'usernames': {
            'admin': {
                'name': 'Admin',
                'password': stauth.Hasher(['123']).generate()[0]  # Hashed password
            }
        }
    },
    'cookie': {
        'name': 'cookie_name',
        'key': 'signature_key',
        'expiry_days': 1
    },
    'preauthorized': {
        'emails': []
    }
}

# Create authenticator object
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
)

# ------------- LOGIN -------------------

name, auth_status, username = authenticator.login('Login', 'main')

if auth_status:
    st.sidebar.success(f"Welcome *{name}*!")

    # Add logout button
    authenticator.logout('Logout', 'sidebar')
    st.sidebar.write("You are logged in.")

    # --------- DATABASE CONNECTION --------
    try:
        engine = create_engine(f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}")
        connection = engine.connect()
    except Exception as e:
        st.error("Failed to connect to database.")
        st.stop()


    # ---------- SHOW DATA ------------------
    st.subheader("All Records")
    try:
        df = pd.read_sql(f"SELECT * FROM {TABLE_NAME}", connection)
        st.dataframe(df)
    except Exception as e:
        st.error("Error fetching data.")


    # --------- INSERT FORM -----------------
    st.subheader("Add New Entry")
    with st.form("entry_form"):
        name_input = st.text_input("Name")
        age_input = st.number_input("Age", min_value=0)
        submitted = st.form_submit_button("Submit")
    

        if submitted:
            if name_input:
                query = text(f"INSERT INTO {TABLE_NAME} (name, age) VALUES (:name, :age)")
                connection.execute(query, {"name": name_input, "age": age_input})
                connection.commit()
                st.success("New entry added.")
            else:
                st.warning("Please fill all fields.")


elif auth_status is False:
    st.error("Invalid username or password.")
elif auth_status is None:
    st.info("Please enter your login credentials.")