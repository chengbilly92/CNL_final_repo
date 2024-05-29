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
        st.session_state['tologin'] = True
    except:
        traceback.print_exc()
        st.error("Register Failed!")
    finally:
        con.close()
    
def main()-> None:
    if 'tologin' in st.session_state:
        del st.session_state['tologin']
        st.switch_page('index.py')
    st.title('Sign up')
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    st.button('register', on_click=lambda: register(username, password))

if __name__ == "__main__":
    main()
