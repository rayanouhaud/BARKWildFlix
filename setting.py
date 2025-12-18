import streamlit as st
import pandas as pd
from database import MaJDataBase
from auth import df

st.header(":violet[**Parametres**]")
st.write("---")

def SetLangue():
    st.write("Dans quel langue voulez-vous mettre le site !")
    cols = st.columns(2)
    with cols[0]:
        if st.button("*Francais*", type="primary") and st.session_state["langues"] == "Anglais":
            st.success("Langues en francais")
            st.session_state["langues"] = "Francais"
    with cols[1]:
        if st.button("*Anglais*", type="primary") and st.session_state["langues"] == "Francais":
            st.success("Langues en Anglais")
            st.session_state["langues"] = "Anglais"

if st.session_state["authentication_status"]:
    if st.session_state["role"] == "admin":
        st.write(":violet[**Voici les paramètres en tant qu'administrateur**]")
        SetLangue()
        st.write("**Mettre à jour la DataBase :**")
        if st.button("MaJ", type="primary"):
            MaJDataBase()
        st.write("Voulez-vous supprimer un compte ?")
        filmName = st.text_input("*Entrez :*")
        if st.form_submit_button("Valider l'utilisateur a supprimer", type="primary"):
            st.success(f"L'utilisateur a été supprimé")
        st.write("**Tous les utilisateurs :**")
        st.dataframe(df)
    else:
        st.write(":violet[**Voici les paramètres en tant qu'utilisateur**]")
        SetLangue()
elif st.session_state["authentication_status"] is False or st.session_state["authentication_status"] is None:
    st.write("**Mais pour ceci il faut être connecté.**")

#Il y aura une page de paramétrage qui permettra d’indiquer plusieurs informations
# telles que : choix du nombre de films à proposer,  choix pour n’indiquer que les films
# avec une certaine durée, que les films en noir et blanc ou en couleur,
# uniquement les films adapté à toutes les classes d'âge, que les films d’un certain genre…