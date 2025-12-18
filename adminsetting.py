import streamlit as st
from auth import load_users, get_authenticator
from database import getDataBase, dbCheckContent, dbNettoyage, getDbApi, dbNettoyageAlgo

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

def MaJDataBase():
  mapping = {'movie_title' : 'Title', 'director_name' : 'Director', 'duration' : 'Runtime', 'genres' : 'Genre', 'language' : 'Language', 'title_year' : 'Year', 'imdb_score' : 'imdb Votes', 'country' : 'Country', 'plot_keywords' : 'Plot', 'actor_1_name' : 'Actors', 'actor_2_name' : 'Actors', 'actor_3_name' : 'Actors'}
  dbFilm = getDataBase("https://drive.google.com/uc?id=1QNf0y3EZ7AZZBocYtfbEJlVSmHxruS5k")
  dbFilm = dbCheckContent(dbFilm, getDbApi(), mapping)
  dbFilm = dbNettoyage(dbFilm)
  dbFilmAlgo = dbNettoyageAlgo(dbFilm)
  dbFilm["movie_title"] = dbFilm["movie_title"].astype(str).str.strip()
  dbFilm.to_csv("dataBaseFilm.csv", index=False)
  dbFilmAlgo.to_csv("dataBaseAlgo.csv", index=False)
  st.success("La DataBase a bien été mis à jour")

def deleteUser(userName):
    user = load_users()
    user.drop([user.index[user["name"] == userName]][0], inplace=True)
    st.success(f"L'utilisateur a été supprimé")
    user.to_csv("login.csv", index=False)
    
def addUser(tempUserName, tempPassword, tempMail, tempRole):
    user = load_users()
    newUser = {"name" : tempUserName, "password" : tempPassword, "email" : tempMail, "failed_login_attemps" : 0, "logged_in" : False, "role" : tempRole}
    user.loc[len(user)] = newUser
    st.success(f"L'utilisateur a été crée")
    user.to_csv("login.csv", index=False)

def settingForAdmin():
    user = load_users()
    st.write(":violet[**Voici les paramètres en tant qu'administrateur**]")
    tabs = st.tabs(["Utilisateur", "Base de donnes", "Statistique"])
    with tabs[0]:
        SetLangue()
    with tabs[1]:
        st.write("**Mettre à jour la DataBase :**")
        if st.button("MaJ", type="primary"):
            MaJDataBase()
        with st.form(key="buttonDeleteUser"):
            st.write("Voulez-vous supprimer un compte ?")
            userName = st.text_input("*Entrez :*")
            if st.form_submit_button("Valider", type="primary"):
                if userName in user["name"].values and not user.loc[user["name"] == userName, "role"].eq("admin").any():
                    deleteUser(userName)
                elif user.loc[user["name"] == userName, "role"].eq("admin").any():
                    st.error("Cet utilisateur est un admin.")
                else:
                    st.error("Cet utilisateur est introuvable.")
        with st.form(key="buttonAddUser"):
            st.write("Voulez-vous ajoutez un compte ?")
            tempUserName = st.text_input("*Son nom d'utilisateur :*")
            tempPassword = st.text_input("*Son mot de passe :*")
            tempMail = st.text_input("*Son mail :*")
            tempRole = st.text_input("*Son nom role :*")
            if st.form_submit_button("Valider", type="primary"):
                if tempUserName in user["name"].values:
                    st.error("Cet utilisateur existe déjà.")
                elif tempUserName is not None and tempPassword is not None and tempMail is not None and tempRole is not None:
                    addUser(tempUserName, tempPassword, tempMail, tempRole)
                else:
                    st.error("Il manque des données pour créer ce compte.")
        st.write("**Tous les utilisateurs :**")
        st.dataframe(user)