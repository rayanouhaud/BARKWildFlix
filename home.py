import streamlit as st
import pandas as pd
from database import dataBaseAlgo, dataBaseFilm

st.title("WILD FLIX")

top10 = dataBaseFilm.sort_values(by="popularity_score", ascending=False).head(10)

print(top10)
with st.form(key="button_form"):
    st.subheader("Votre dernier film visionné")
    test = st.text_input("Entrez :")
    st.form_submit_button("Valider le film")
    st.write(test)

st.subheader("Top 10 des films les plus populaires !")
for i, (_, film) in enumerate(top10.iterrows(), start=1):
    with st.container(border=True):
        st.write(f"{i}: {film['movie_title']}")