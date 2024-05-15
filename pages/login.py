import streamlit as st
import sqlite3

def checkLogin(username: str, password: str)-> None:
    con = sqlite3.Connection('user.db')
    cur: sqlite3.Cursor = con.cursor()
    res = cur.execute('SELECT password FROM users WHERE username = ?;', (username,))

    if password == res.fetchone()[0]:
        st.success("Login successful!")
        st.session_state['login'] = username
    elif username != "" or password != "":
        st.error("Invalid username or password.")

def main():
    st.title("Simple Login Page")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    st.button('Login', on_click=lambda: checkLogin(username, password))

if __name__ == "__main__":
    main()