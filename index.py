import streamlit as st
from streamlit import runtime
from streamlit.runtime.scriptrunner import get_script_run_ctx
from streamlit.web.server.websocket_headers import _get_websocket_headers
import requests
import st_pages
from st_pages import Page

def get_remote_ip() -> str:
    ctx = get_script_run_ctx()
    if not ctx: return None
    session_info = runtime.get_instance().get_client(ctx.session_id)
    if not session_info: return None
    return session_info.request.remote_ip

def get_forwarded_ip()-> str:
    headers = _get_websocket_headers()
    try:
        x_forwarded_for = headers['X-Forwarded-For']
    except KeyError:
        return get_remote_ip()
    first_ip = x_forwarded_for.split(', ')[0]
    return first_ip

@st.cache_data
def get_ip_info(user_ip: str)-> dict:
    r: requests.Response = requests.get(f'http://ip-api.com/json/{user_ip}')
    return r.json()

def set_sidebar()-> None:
    if 'login' in st.session_state: 
        st_pages.show_pages([
            Page('index.py', 'Home'),
            Page('pages/chat.py', 'Chat'),
            Page('pages/logout.py', 'Log Out'),
            Page('pages/changePassword.py', 'Change Password')
        ])
        st_pages.hide_pages(["Another page"])
    else:
        st_pages.show_pages([
            Page('index.py', 'Home'),
            Page('pages/register.py', 'Sign up'),
            Page('pages/login.py', 'Log In')
        ])
        st_pages.hide_pages(["Another page"])

def main()-> None:
    set_sidebar()
    if 'login' in st.session_state: 
        st.title(f'Hello:\t{st.session_state["login"]}.')
    else:
        st.title(f'Hello:\tGuest.')

    user_ip: str = get_forwarded_ip()
    st.text(f'Your ip address: {user_ip}')
    user_ip_info: dict = get_ip_info(user_ip)
    if user_ip_info['status'] == "success":
        st.write(f'Your country: {user_ip_info["country"]}')
    st.session_state['userip'] = "localhost" if user_ip_info['status'] == "fail" else user_ip

if __name__ == "__main__":
    main()

