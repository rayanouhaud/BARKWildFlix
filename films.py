import streamlit as st
import pandas as pd

st.header("Liste des films")
if st.session_state["authentication_status"]:
    st.write("salut")