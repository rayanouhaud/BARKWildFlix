import streamlit as st
import pandas as pd
from affiche import getAffiche, BadValue, makeAffichage
from database import getDataBaseFilm

dataBaseFilm = getDataBaseFilm()

st.header(":violet[**Liste des films**]")
if st.session_state["authentication_status"] != True:
    st.write("**Pour voir la totalité des film vous devez vous connecter !**")
st.write("---")

cols = st.columns(2)

if st.session_state["authentication_status"]:
    for id, film in dataBaseFilm.iterrows():
        makeAffichage(id)
else:
    film20 = dataBaseFilm.head(20)
    for id, film in film20.iterrows():
        makeAffichage(id)