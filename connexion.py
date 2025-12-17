from streamlit_authenticator import Authenticate
import streamlit as st
import pandas as pd
from auth import get_authenticator
from auth import dataUser


if st.session_state.get("authentication_status"):
    st.header("Deconnexion")
else:
    st.header("Connexion")

authenticator = get_authenticator(dataUser)
authenticator.login()

if st.session_state["authentication_status"]:
    st.success(f"Bienvenue Utilisateur !")
    authenticator.logout("Déconnexion")
elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect")