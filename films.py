import streamlit as st
import pandas as pd
from affiche import getAffiche
from database import dataBaseFilm


st.header(":violet[**Liste des films**]")
if st.session_state["authentication_status"] != True:
    st.write("**Pour voir la totalité des film vous devez vous connecter !**")
st.write("---")

cols = st.columns(2)

if st.session_state["authentication_status"]:
    for _, film in dataBaseFilm.iterrows():
        with cols[0]:
            st.image(getAffiche(film['movie_title']))
        with cols[1].container(height=516):
            st.write(f"**{film['movie_title']}**")
            st.write(f"Création originale {film['director_name']}")
else:
    film20 = dataBaseFilm.head(20)
    for _, film in film20.iterrows():
        with cols[0]:
            st.image(getAffiche(film['movie_title']))
        with cols[1].container(height=516):
            st.write(f"{film['movie_title']}")
            st.write(f"**Création originale** {film['director_name']}")

