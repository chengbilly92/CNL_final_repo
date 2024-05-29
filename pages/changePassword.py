import streamlit as st
import sqlite3
import traceback
def get_stored_password(username):
    con = sqlite3.connect('user.db')
    cur: sqlite3.Cursor = con.cursor()
    
    try:
        # cur.execute('SELECT password FROM users WHERE username = ?;', (username,))
        result = cur.execute('SELECT password FROM users WHERE username = ?;', (username,)).fetchone()
        return result[0] if result else None
    except sqlite3.Error as e:
        # print(f"An error occurred: {e}")
        st.error(f"Internal Server Error: {e}")
        return None
    finally:
        con.close()

def verify_password(stored_password, provided_password):
    return stored_password == provided_password

def update_password(username, new_password):
    con = sqlite3.connect('user.db')
    cur = con.cursor()
    try:
        cur.execute('UPDATE users SET password = ? WHERE username = ?', (new_password, username))
        con.commit()
        st.success("Password updated successfully.")
        st.session_state['tologin'] = True
    except sqlite3.Error as e:
        # print(f"An error occurred: {e}")
        traceback.print_exc()
        st.error(f"Internal Server Error: {e}")
    finally:
        con.close()

def change_password(username, old_password, new_password):
    stored_password = get_stored_password(username)
    
    if stored_password and verify_password(stored_password, old_password):
        update_password(username, new_password)
    else:
        st.error("The original password is incorrect.")
def main()-> None:
    if 'tologin' in st.session_state:
        del st.session_state['tologin']
        del st.session_state['login']
        st.switch_page('index.py')
    st.text("You've now logged in as {}.".format(st.session_state.login))
    st.title('Change Password')
    oldPassword = st.text_input("Old Password", type="password")
    password = st.text_input("New Password", type="password")

    st.button('change', on_click=lambda: change_password(st.session_state.login, oldPassword, password))

if __name__ == "__main__":
    main()


