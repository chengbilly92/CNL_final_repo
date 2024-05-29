import streamlit as st
import st_pages
from st_pages import Page

def set_sidebar()-> None:
    if 'login' in st.session_state: 
        st_pages.show_pages([
            Page('index.py', 'Home'),
            Page('pages/chat.py', 'Chat'),
            Page('pages/logout.py', 'Log Out'),
            Page('pages/changePassword.py', 'Change Password')
        ])
        st_pages.hide_pages(["Another page"])
    else:
        st_pages.show_pages([
            Page('index.py', 'Home'),
            Page('pages/register.py', 'Sign up'),
            Page('pages/login.py', 'Log In')
        ])
        st_pages.hide_pages(["Another page"])