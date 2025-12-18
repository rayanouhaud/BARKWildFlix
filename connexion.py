import streamlit as st
import pandas as pd
from auth import get_authenticator, dataUser, user
import streamlit_authenticator as stauth

if st.session_state.get("authentication_status"):
    st.header(":violet[**Deconnexion**]")
else:
    st.header(":violet[**Connexion**]")
st.write("---")

authenticator = get_authenticator(dataUser)
try:
    authenticator.login()
except stauth.utilities.exceptions.LoginError:
    st.error("Utilisateur non autorisé ou supprimé")

if st.session_state["authentication_status"]:
    st.session_state["role"] = user[user["name"] == st.session_state["name"]].iloc[0]["role"]
    st.success(f"Bienvenue {st.session_state["name"]} !")
    if authenticator.logout("Déconnexion"):
        st.session_state["authentication_status"] = None
        st.session_state.user = "Nobody"
        st.session_state["neighbors"] = 5
elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect")