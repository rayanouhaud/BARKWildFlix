import streamlit as st
import pandas as pd
from database import getDataBaseAlgo, getDataBaseFilm
from affiche import getAffiche, makeAffichage
from algo import AlgoRecoFilm

st.title(":violet[**WILD FLIX**]")
st.write("---")

dataBaseFilm = getDataBaseFilm()
top10 = dataBaseFilm.sort_values(by="popularity_score", ascending=False).head(10)
writeFilm = 0

with st.form(key="button_form"):
    st.subheader("Votre dernier film visionné")
    filmName = st.text_input("*Entrez :*")
    if st.form_submit_button("Valider le film", type="primary"):
        if filmName in dataBaseFilm["movie_title"].values:
            writeFilm = 1
            st.success("Votre film a été trouvé !")
            makeAffichage(dataBaseFilm.index[dataBaseFilm["movie_title"] == filmName][0], contain=False)
            algoIndex = AlgoRecoFilm(filmName, st.session_state["neighbors"])
        else:
            st.error("Votre film n'a pas été trouvé.")
            writeFilm = 0

if writeFilm == 1:
    st.subheader("Après avoir vu ce film, nous vous recommandons :")
    cols = st.columns(2)
    with cols[0]:
        for i in range(st.session_state["neighbors"]):
            if i != 0:
                with cols[(i - 1) % 2]:
                    makeAffichage(algoIndex[0][i], level=1, contain=False)
                    st.write("---")

if writeFilm == 0:
    st.subheader("Top 10 des films les plus populaires !")
    cols = st.columns(3)
    for i, (_, film) in enumerate(top10.iterrows(), start=1):
        with cols[(i - 1) % 3].container(border=True):
            st.write(f"**Numéro {i}:** {film['movie_title']}")
            st.image(getAffiche(film['movie_title']))
