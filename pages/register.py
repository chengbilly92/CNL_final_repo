import streamlit as st
import sqlite3
import traceback
import utils
import time

def register(username: str, password: str)-> None:
    try:
        con = sqlite3.Connection('user.db')
        if not username or not password:
            return
        cur: sqlite3.Cursor = con.cursor()
        cur.execute('INSERT INTO users(username, password) VALUES (?, ?);', (username, password,))
        con.commit()
        st.success("Successfully registered!")
        st.session_state['tologin'] = True
    except sqlite3.IntegrityError as err:
        st.error('Username have been used')
    except:
        traceback.print_exc()
        st.error("Register Failed!")
    finally:
        con.close()
    
def main()-> None:
    utils.set_sidebar()
    st.title(st.session_state['country'])

    with st.form("signupform"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submited = st.form_submit_button('register')
        if submited:
            try:
                con = sqlite3.Connection('user.db')
                cur: sqlite3.Cursor = con.cursor()
                cur.execute('INSERT INTO users(username, password) VALUES (?, ?);', (username, password,))
                con.commit()
                st.success("Successfully registered!")
                st.session_state['tologin'] = True
            except sqlite3.IntegrityError as err:
                st.error('Username have been used')
            except:
                traceback.print_exc()
                st.error("Register Failed!")
            finally:
                con.close()

    if 'tologin' in st.session_state:
        del st.session_state['tologin']
        time.sleep(0.5)
        st.switch_page('index.py')

if __name__ == "__main__":
    main()
