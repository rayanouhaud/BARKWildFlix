import streamlit as st
import pandas as pd
from auth import get_authenticator, load_users, build_credentials
import streamlit_authenticator as stauth
from adminsetting import addUser

user = load_users()

if st.session_state.get("authentication_status"):
    st.header(":violet[**Deconnexion**]")
else:
    st.header(":violet[**Connexion**]")
st.write("---")

tabs = st.tabs(["Connexion", "Créer un compte"])

with tabs[0]:
    authenticator = get_authenticator()
    try:
        authenticator.login()
    except stauth.utilities.exceptions.LoginError:
        st.error("Utilisateur non autorisé ou supprimé")
    if st.session_state["authentication_status"] and not user[user["name"] == st.session_state.get("name")].empty:
        st.session_state["role"] = user[user["name"] == st.session_state["name"]].iloc[0]["role"]
        st.success(f"Bienvenue {st.session_state["name"]} !")
        user.loc[user["name"] == st.session_state["name"], "logged_in"] = True
        user.to_csv("login.csv", index=False)
        if authenticator.logout("Déconnexion"):
            st.session_state["authentication_status"] = None
            st.session_state.user = "Nobody"
            st.session_state["neighbors"] = 5
    elif st.session_state["authentication_status"] is False:
        st.error("L'username ou le password est/sont incorrect")

with tabs[1]:
    if st.session_state["authentication_status"] is False or st.session_state["authentication_status"] is None:
        with st.form(key="buttonCreateUser"):
            st.write("Créer son compte ?")
            tempUserName = st.text_input("*Son nom d'utilisateur :*")
            tempPassword = st.text_input("*Son mot de passe :*")
            tempMail = st.text_input("*Son mail :*")
            if st.form_submit_button("Valider", type="primary"):
                if tempUserName in user["name"].values:
                    st.error("Cet utilisateur existe déjà.")
                elif tempUserName is not None and tempPassword is not None and tempMail is not None:
                    addUser(tempUserName, tempPassword, tempMail, "user")
                else:
                    st.error("Il manque des données pour créer ce compte.")
    else:
        st.success("Vous êtes connectés !")
