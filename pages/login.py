import streamlit as st
import sqlite3
import traceback
import utils
import time

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
    st.title(utils.LogIn[st.session_state['country']])

    with st.form('loginform'):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submited = st.form_submit_button('Login')
        if submited:
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

    if 'login' in st.session_state:
        time.sleep(0.5)
        st.switch_page('index.py')

if __name__ == "__main__":
    main()
