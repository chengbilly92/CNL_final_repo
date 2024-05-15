import streamlit as st

if 'login' in st.session_state:
    del st.session_state['login']

st.switch_page('index.py')
