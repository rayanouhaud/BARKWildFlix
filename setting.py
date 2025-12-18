import streamlit as st
import pandas as pd
from auth import get_authenticator
from adminsetting import settingForAdmin, SetLangue, deleteUser
from database import getDataBaseFilm

st.header(":violet[**Parametres**]")
st.write("---")

dataBaseFilm = getDataBaseFilm()

if st.session_state["authentication_status"]:
    if st.session_state["role"] == "admin":
        settingForAdmin()
    else:
        st.write(":violet[**Voici les paramètres en tant qu'utilisateur**]")
        SetLangue()
        st.session_state["neighbors"] = int(st.select_slider(
            "Le nombre de film à recommander",
            options=[
                "2",
                "3",
                "4",
                "5",
                "5",
                "6",
                "7",
            ]
            )) + 1
        all_genres = dataBaseFilm["genres"].str.split("|").explode().str.strip().unique().tolist()
        chooseGenre = st.multiselect(
            "Quel(s) genre(s) de film voulez vous voir ?",
            all_genres
        )
        st.session_state["genre"] = chooseGenre
elif st.session_state["authentication_status"] is False or st.session_state["authentication_status"] is None:
    st.write("**Mais pour ceci il faut être connecté.**")

#Il y aura une page de paramétrage qui permettra d’indiquer plusieurs informations
# telles que : choix du nombre de films à proposer,  choix pour n’indiquer que les films
# avec une certaine durée, que les films en noir et blanc ou en couleur,
# uniquement les films adapté à toutes les classes d'âge, que les films d’un certain genre…
