import streamlit as st
import sqlite3
import time
import traceback

@st.experimental_dialog("Please log in")
def loginFail()-> None:
    b: bool = st.button("Go to log in page")
    if b:
        st.switch_page('pages/login.py')

def main()-> None:
    try:
        con = sqlite3.Connection('user.db')
        cur: sqlite3.Cursor = con.cursor()
        content: str = st.text_input("Say something!!")
        if content:
            cur.execute('INSERT INTO messages VALUES (?, ?, ?)', (st.session_state["login"], content, time.time(),))
            con.commit()
            content = ''
        res: list[tuple] = cur.execute('SELECT * FROM messages;')
        for m in res:
            st.text(f'{m[0]}: {m[1]}')
    except:
        traceback.print_exc()
        st.error("Internal Server Error.")
    finally:
        con.close()
    

if 'login' in st.session_state and st.session_state['login']:
    main()
else: 
    loginFail()
