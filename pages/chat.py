import streamlit as st
import sqlite3
import traceback
from datetime import datetime
import utils
from googletrans import Translator

def main()-> None:
    utils.set_sidebar()
    language = st.session_state['language']
    translator = Translator()
    message = str()
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
            message += f'{m[0]}({m[1]}): {translator.translate(m[2], dest=language).text}\n'
        st.text(message)
    except:
        traceback.print_exc()
        st.error("Internal Server Error.")
    finally:
        con.close()
    
if 'login' in st.session_state and st.session_state['login']:
    main()
else: 
    st.switch_page('index.py')
