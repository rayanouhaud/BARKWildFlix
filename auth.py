import streamlit as st
import streamlit_authenticator as stauth
import pandas as pd

def load_users():
    return pd.read_csv("login.csv")

def build_credentials():
    user = load_users()
    dataUser = {"usernames": {}}
    for _, row in user.iterrows():
        dataUser["usernames"][row["name"]] = {
            "name": row["name"],
            "password": row["password"],
            "email": row["email"],
            "role": row["role"],
            "failed_login_attemps": row["failed_login_attemps"],
        }
    return dataUser

def get_authenticator():
    dataUser = build_credentials()
    if "authenticator" not in st.session_state:
        st.session_state.authenticator = stauth.Authenticate(
            dataUser,
            "cookie_name",
            "cookie_key",
            30
        )
    return st.session_state.authenticator