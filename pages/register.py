import streamlit as st
import sqlite3
import traceback

def register(username: str, password: str)-> None:
    try:
        con = sqlite3.Connection('user.db')
        cur: sqlite3.Cursor = con.cursor()
        cur.execute('INSERT INTO users(username, password) VALUES (?, ?);', (username, password,))
        con.commit()
        st.success("Successfully registered!")
    except:
        traceback.print_exc()
        st.error("Register Failed!")
    finally:
        con.close()
    

def main()-> None:
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    st.button('register', on_click=lambda: register(username, password))
   

if __name__ == "__main__":
    main()