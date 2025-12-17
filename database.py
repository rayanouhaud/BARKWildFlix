import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import NearestNeighbors
import numpy as np
import streamlit as st

dbApi = pd.read_csv("dataBaseApi.csv", sep= ",")
dataBaseFilm = pd.read_csv("dataBaseFilm.csv")
dataBaseAlgo = pd.read_csv("dataBaseAlgo.csv")

def getDataBase(url):
    dbFilm = pd.read_csv(url ,sep= ",")
    return dbFilm

def dbCheckContent(dbFilm, dbClean, mapping):
  for col in dbFilm.columns: # traverse colonne de dbFilm
    for index, value in dbFilm[col].items(): # traverse ligne de dbFilm
      if col == 'color': # si la colonne est 'color' alors met tout avec la valeur 'Color'
        value = 'Color'
      if mapping.get(col) is not None and (value == 'N/A' or pd.isna(value)): # si la colonne existe dans L'API et la valeur de la ligne est NULL ou egale a N/A alors remplace avec valeur de l'API
        value = dbClean[mapping.get(col)][index]
        if 'United States' in value:
          value = value.replace("United States", "USA")
        if 'United Kingdom' in value:
          value = value.replace("United Kingdom", "UK")
        if col == 'duration' and value != 'N/A':
          value = float(value.split()[0])                     # separe la chaine de caractere entre
        if col == 'language':
          value = "English"
        if col == 'country' and dbFilm['language'][index] == 'English':
          value = 'USA'
      dbFilm.at[index, col] = value
    return dbFilm

def dbNettoyage(dbFilm):
  for col in dbFilm.columns:
    if dbFilm[col].dtype in [int, float, "float64", "int64"]:
        dbFilm[col] = dbFilm[col].fillna(0)  # NaN → 0
    elif dbFilm[col].dtype == object:
        dbFilm[col] = dbFilm[col].replace("", np.nan)  # considérer "" comme NaN
        dbFilm[col] = dbFilm[col].fillna("Inconnu") 
  return dbFilm

def dbNettoyageAlgo(dbFilm):
    filtreAlgo = ['duration', 'genres', 'title_year', 'gross', 'budget', 'imdb_score', 'plot_keywords']
    filtreAntiAlgo = [col for col in dbFilm.columns if col not in filtreAlgo]

    filtrePopularity = ['director_facebook_likes', 'actor_1_facebook_likes', 'actor_2_facebook_likes', 'actor_3_facebook_likes', 'num_voted_users', 'num_critic_for_reviews']
    for col in filtrePopularity:
        dbFilm[col] = dbFilm[col].fillna(0)
    dbFilm['popularity_score'] = (2*dbFilm['director_facebook_likes'] + 2*dbFilm['actor_1_facebook_likes'] + 1.5*dbFilm['actor_2_facebook_likes'] + 1*dbFilm['actor_3_facebook_likes']    + 1*dbFilm['num_voted_users'] + 0.5*dbFilm['num_critic_for_reviews'])

    dbFilmAlgo = dbFilm.drop(columns=filtreAntiAlgo)
    for filtre in filtreAlgo:
        if filtre == 'plot_keywords':
            dbFilmAlgo[filtre] = dbFilmAlgo[filtre].fillna('unknown')
        elif filtre != 'genres':
            dbFilmAlgo[filtre] = dbFilmAlgo[filtre].fillna(dbFilmAlgo[filtre].median())

    dbFilmAlgo['plot_keywords_split'] = dbFilmAlgo['plot_keywords'].str.split('|')
    dbFilmAlgo['plot_keywords_joined'] = dbFilmAlgo['plot_keywords_split'].apply(lambda x: ' '.join(x))
    plot_dummies = dbFilmAlgo['plot_keywords_joined'].str.get_dummies(sep=' ')
    dbFilmAlgo = pd.concat([dbFilmAlgo, plot_dummies], axis=1)
    dbFilmAlgo = dbFilmAlgo.drop(columns=['plot_keywords', 'plot_keywords_split', 'plot_keywords_joined'])

    dbFilmAlgo['genres_split'] = dbFilmAlgo['genres'].str.split('|')
    genres_dummies = dbFilmAlgo['genres_split'].str.join('|').str.get_dummies()
    dbFilmAlgo = pd.concat([dbFilmAlgo, genres_dummies], axis=1)
    dbFilmAlgo = dbFilmAlgo.drop(columns=['genres', 'genres_split'])

    scaler = MinMaxScaler()
    dbScaled = pd.DataFrame(scaler.fit_transform(dbFilmAlgo), columns=dbFilmAlgo.columns)
    return dbScaled

def MaJDataBase():
    mapping = {'movie_title' : 'Title', 'director_name' : 'Director', 'duration' : 'Runtime', 'genres' : 'Genre', 'language' : 'Language', 'title_year' : 'Year', 'imdb_score' : 'imdb Votes', 'country' : 'Country', 'plot_keywords' : 'Plot', 'actor_1_name' : 'Actors', 'actor_2_name' : 'Actors', 'actor_3_name' : 'Actors'}
    dbFilm = getDataBase("https://drive.google.com/uc?id=1QNf0y3EZ7AZZBocYtfbEJlVSmHxruS5k")
    dbFilm = dbCheckContent(dbFilm, dbApi, mapping)
    dbFilm = dbNettoyage(dbFilm)
    dbFilmAlgo = dbNettoyageAlgo(dbFilm)
    dbFilm.to_csv("dataBaseFilm.csv", index=False)
    dbFilmAlgo.to_csv("dataBaseAlgo.csv", index=False)
    st.success("La DataBase a bien été mis à jour")