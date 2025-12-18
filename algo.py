import streamlit as st
import pandas as pd
from sklearn.neighbors import NearestNeighbors
from database import getDataBaseAlgo, getDataBaseFilm

def AlgoRecoFilm(filmName, n):
    dataBaseAlgo = getDataBaseAlgo()
    dataBaseFilm = getDataBaseFilm()
    dataBaseIndex = dataBaseFilm.index[dataBaseFilm["movie_title"] == filmName]
    model = NearestNeighbors(n_neighbors=n)
    model.fit(dataBaseAlgo)
    distances, indices = model.kneighbors(dataBaseAlgo.iloc[[dataBaseIndex[0]]])
    return indices