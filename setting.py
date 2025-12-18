import streamlit as st
import pandas as pd
from auth import get_authenticator
from adminsetting import settingForAdmin, SetLangue

st.header(":violet[**Parametres**]")
st.write("---")

if st.session_state["authentication_status"]:
    if st.session_state["role"] == "admin":
        settingForAdmin()
    else:
        st.write(":violet[**Voici les paramètres en tant qu'utilisateur**]")
        SetLangue()
elif st.session_state["authentication_status"] is False or st.session_state["authentication_status"] is None:
    st.write("**Mais pour ceci il faut être connecté.**")

#Il y aura une page de paramétrage qui permettra d’indiquer plusieurs informations
# telles que : choix du nombre de films à proposer,  choix pour n’indiquer que les films
# avec une certaine durée, que les films en noir et blanc ou en couleur,
# uniquement les films adapté à toutes les classes d'âge, que les films d’un certain genre…