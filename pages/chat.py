import streamlit as st
import sqlite3
import traceback
from datetime import datetime
import utils
import signal

def handler(signum, frame):
    st.rerun()

def main()-> None:
    utils.set_sidebar()
    signal
    signal.alarm(3)
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
    st.switch_page('index.py')
