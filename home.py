import streamlit as st
import pandas as pd
from database import dataBaseAlgo, dataBaseFilm
from affiche import getAffiche

st.title(":violet[**WILD FLIX**]")
st.write("---")

top10 = dataBaseFilm.sort_values(by="popularity_score", ascending=False).head(10)

with st.form(key="button_form"):
    st.subheader("Votre dernier film visionné")
    filmName = st.text_input("*Entrez :*")
    st.form_submit_button("Valider le film", type="primary")
    st.write(filmName)

st.subheader("Top 10 des films les plus populaires !")
for i, (_, film) in enumerate(top10.iterrows(), start=1):
    with st.container(border=True):
        st.write(f"**Numéro {i}:** {film['movie_title']}")
        st.image(getAffiche(film['movie_title']))
