import streamlit as st
import sqlite3
import traceback
from datetime import datetime
from streamlit_autorefresh import st_autorefresh
import utils

@st.experimental_dialog("Please log in")
def login_fail()-> None:
    b: bool = st.button("Go to log in page")
    if b:
        st.switch_page('pages/login.py')

def main()-> None:
    utils.set_sidebar()
    st_autorefresh(1000)
    try:
        con = sqlite3.Connection('user.db')
        cur: sqlite3.Cursor = con.cursor()
        content: str = st.chat_input("Say something!!")
        if content:
            cur.execute('INSERT INTO messages VALUES (?, ?, ?, ?)',(
                st.session_state["login"],
                st.session_state['userip'],
                content, 
                datetime.now().strftime('%Y/%m/%d, %H:%M:%S')
            ))
            con.commit()
            content = ''
        
        res: list[tuple] = cur.execute('SELECT * FROM messages;')
        for m in res:
            
            st.text(f'{m[0]}({m[1]}): {m[2]}')
    except:
        traceback.print_exc()
        st.error("Internal Server Error.")
    finally:
        con.close()
    
if 'login' in st.session_state and st.session_state['login']:
    main()
else: 
    login_fail()
