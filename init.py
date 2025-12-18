import streamlit as st
import pandas as pd

if 'current_page' not in st.session_state:
    st.session_state.current_page = "Home"

if "role" not in st.session_state:
    st.session_state["role"] = "Nobody"

if "authentication_status" not in st.session_state:
    st.session_state["authentication_status"] = None

if "langues" not in st.session_state:
    st.session_state["langues"] = "Francais"

if "neighbors" not in st.session_state:
    st.session_state["neighbors"] = 5

with st.sidebar:
    st.write("")

pages = [
    st.Page(
        "home.py",
        title="Accueil",
        icon=":material/home:"
    ),
    st.Page(
        "films.py",
        title="Liste des Films",
        icon=":material/article:"
    ),
    st.Page(
        "stat.py",
        title="Statistiques",
        icon=":material/insert_chart:"
    ),
    st.Page(
        "setting.py",
        title="Paramètres",
        icon=":material/error:"
    ),
]

if st.session_state.get("authentication_status"):
    pages.append(st.Page(
            "connexion.py",
            title="Déconnectez-vous",
            icon=":material/logout:"
        ))
else:
    pages.append(st.Page(
            "connexion.py",
            title="Connectez-vous",
            icon=":material/login:"
        ))

page = st.navigation(pages)
page.run()
