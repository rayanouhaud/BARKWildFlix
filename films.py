import streamlit as st
import pandas as pd
from affiche import getAffiche
from database import dataBaseFilm


st.header(":violet[**Liste des films**]")
if st.session_state["authentication_status"] != True:
    st.write("**Pour voir la totalité des film vous devez vous connecter !**")
st.write("---")

cols = st.columns(2)

def BadValue(value):
    if type(value) == "int" or type(value) == float:
        if value == 0:
            return "Non connu"
        return int(value)
    if value == "Inconnu":
        return "Non connu"
    return value

if st.session_state["authentication_status"]:
    for _, film in dataBaseFilm.iterrows():
        with cols[0]:
            st.image(getAffiche(film['movie_title']))
        with cols[1].container(height=516):
            st.write(f":violet[**{film['movie_title']}**]")
            st.write(f"Création originale {film['director_name']}")
else:
    film20 = dataBaseFilm.head(20)
    for _, film in film20.iterrows():
        with cols[0]:
            st.image(getAffiche(film['movie_title']))
        with cols[1].container(height=516):
            st.write(f"**:violet[{BadValue(film['movie_title'])}]**")
            st.write(f"**Création originale :** {BadValue(film['director_name'])}")
            st.write(f"**Durée (en minutes) :** {BadValue(film['duration'])}")
            st.write(f"**Acteurs :** {BadValue(film['actor_1_name'])}, {BadValue(film['actor_2_name'])}, {BadValue(film['actor_3_name'])}")
            st.write(f"**Genres :** {BadValue(film['genres'].replace("|", ", "))}")
            st.write(f"**Année de sortie :** {BadValue(film['title_year'])}")
            st.write(f"**IMDB Score :** {BadValue(film['imdb_score'])}")
            st.write(f"**Score de popularité:** {BadValue(film['popularity_score'])}")