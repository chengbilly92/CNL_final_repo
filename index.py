import streamlit as st
from streamlit import runtime
from streamlit.runtime.scriptrunner import get_script_run_ctx
from streamlit.runtime.state import session_state
from streamlit.web.server.websocket_headers import _get_websocket_headers
import requests
import utils
from PIL import Image
import os
import random

@st.cache_data
def load_image(image_file):
    img = Image.open(image_file)
    return img

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

def main()-> None:
    utils.set_sidebar()
    if 'login' in st.session_state: 
        st.title(f'Hello:\t{st.session_state["login"]}.')
    else:
        st.title(f'Hello:\tGuest.')
    user_ip: str = get_forwarded_ip()
    st.text(f'Your ip address: {user_ip}')
    user_ip_info: dict = get_ip_info(user_ip)
    print(user_ip_info['status'])
    if user_ip_info['status'] == "success":
        st.write(f'Your country: {user_ip_info["country"]}')
    st.session_state['userip'] = "localhost" if user_ip_info['status'] == "fail" else user_ip
    st.session_state["country"] = "unknown" if user_ip_info['status'] == "fail" else user_ip_info["country"]
    newPath = "./image/{}".format(st.session_state["country"])
    if not os.path.exists(newPath):
        os.makedirs(newPath)
    filePath = "./image/{}".format(st.session_state['country'])
    files = os.listdir(filePath)
    if len(files) == 0:
        st.text("No images for your country.")
    else:
        image_file = random.choice(files)
        img = load_image(filePath+"/"+image_file)
        st.image(img)


if __name__ == "__main__":
    main()

