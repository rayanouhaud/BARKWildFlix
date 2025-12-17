import streamlit as st
import pandas as pd
from auth import get_authenticator, dataUser, df

if st.session_state.get("authentication_status"):
    st.header(":violet[**Deconnexion**]")
else:
    st.header(":violet[**Connexion**]")
st.write("---")

authenticator = get_authenticator(dataUser)
authenticator.login()

if st.session_state["authentication_status"]:
    st.session_state["role"] = df[df["name"] == st.session_state["name"]].iloc[0]["role"]
    st.success(f"Bienvenue {st.session_state["name"]} !")
    authenticator.logout("Déconnexion")
elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect")