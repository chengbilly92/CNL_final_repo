import streamlit as st
import sqlite3
import traceback

def checkLogin(username: str, password: str)-> None:
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
    st.title("Simple Login Page")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    st.button('Login', on_click=lambda: checkLogin(username, password))

if __name__ == "__main__":
    main()