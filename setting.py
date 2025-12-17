import streamlit as st
import pandas as pd

st.header("Parametres")

st.write("Vous pouvez modifier certains réglages sur ce site.")

if st.session_state["authentication_status"]:
    st.write("Langues")
elif st.session_state["authentication_status"] is False or st.session_state["authentication_status"] is None:
    st.write("Mais pour ceci il faut être connecté.")