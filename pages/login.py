import streamlit as st
import sqlite3
import traceback
import utils

def check_login(username: str, password: str)-> None:
    try:
        con = sqlite3.Connection('user.db')
        cur: sqlite3.Cursor = con.cursor()
        res = cur.execute('SELECT password FROM users WHERE username = ?;', (username,)).fetchone()

        if res and password and password == res[0]:
            st.success("Login successful!")
            st.session_state['login'] = username
        else:
            st.error("Invalid username or password.")
    except:
        traceback.print_exc()
        st.error("Invalid username or password.")
    finally:
        con.close()

def main():
    utils.set_sidebar()
    if 'login' in st.session_state:
        st.switch_page('index.py')
    st.title("Simple Login Page")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    st.button('Login', on_click=lambda: check_login(username, password))

if __name__ == "__main__":
    main()
