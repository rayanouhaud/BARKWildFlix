import requests
import pandas as pd
import streamlit as st
from database import getDataBaseFilm

def BadValue(value):
    if isinstance(value, pd.Series):
        value = value.iloc[0]
    if type(value) == "int" or type(value) == float:
        if value == 0 or  value == 0.0:
            return "Non connu"
        return int(value)
    if value == "Inconnu":
        return "Non connu"
    return value

def getAffiche(movie_title):
    api_key = "94487201f2075a6b8c1e7e15a02fe164"
    url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={movie_title}"
    try:
        response = requests.get(url).json()
        results = response.get('results', [])
        if results and results[0].get('poster_path'):
            poster_path = results[0]['poster_path']
            poster_url = f"https://image.tmdb.org/t/p/w500{poster_path}"
            return poster_url
        else:
            return "logo.png"
    except Exception as e:
        return "logo.png"

def makeAffichage(index, level=3, contain=True):
    dataBaseFilm = getDataBaseFilm()
    st.subheader(f"**:violet[{BadValue(dataBaseFilm.iloc[index]['movie_title'])}]**")
    cols = st.columns(2)
    with cols[0]:
        st.image(getAffiche(dataBaseFilm.iloc[index]['movie_title']))
    with cols[1].container(border=contain):
        if level >= 1:
            st.write(f"**Année de sortie :** {BadValue(dataBaseFilm.iloc[index]['title_year'])}")
            st.write(f"**Durée (en minutes) :** {BadValue(dataBaseFilm.iloc[index]['duration'])}")
        if level >= 2:
            st.write(f"**Création originale :** {BadValue(dataBaseFilm.iloc[index]['director_name'])}")
            st.write(f"**Genres :** {BadValue(dataBaseFilm.iloc[index]['genres'].replace('|', ','))}")    
        if level == 3:
            st.write(f"**Acteurs :** {BadValue(dataBaseFilm.iloc[index]['actor_1_name'])}, {BadValue(dataBaseFilm.iloc[index]['actor_2_name'])}, {BadValue(dataBaseFilm.iloc[index]['actor_3_name'])}")
            st.write(f"**IMDB Score :** {BadValue(dataBaseFilm.iloc[index]['imdb_score'])}")

#st.write(f"**:violet[{BadValue(film['movie_title'])}]**")
#st.write(f"**Création originale :** {BadValue(film['director_name'])}")
#st.write(f"**Durée (en minutes) :** {BadValue(film['duration'])}")
#st.write(f"**Acteurs :** {BadValue(film['actor_1_name'])}, {BadValue(film['actor_2_name'])}, {BadValue(film['actor_3_name'])}")
#st.write(f"**Genres :** {BadValue(film['genres'].replace("|", ", "))}")
#st.write(f"**Année de sortie :** {BadValue(film['title_year'])}")
#st.write(f"**IMDB Score :** {BadValue(film['imdb_score'])}")
#st.write(f"**Score de popularité:** {BadValue(film['popularity_score'])}")