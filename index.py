import streamlit as st
from streamlit import runtime
from streamlit.runtime.scriptrunner import get_script_run_ctx
from streamlit.web.server.websocket_headers import _get_websocket_headers
import requests
import utils
import os
import random
from PIL import Image

import base64
@st.cache_data
def load_image(image_file):
    img = Image.open(image_file)
    return img

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    opacity: 0.8;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)


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
    first_reload: bool = (st.session_state["country"] == "unknown")
    user_ip: str = get_forwarded_ip()
    user_ip_info: dict = get_ip_info(user_ip)
    # print(st.session_state)
    st.session_state['userip'] = "localhost" if user_ip_info['status'] == "fail" else user_ip
    if st.session_state["country"] == "unknown":
        st.session_state["country"] = "unknown" if user_ip_info['status'] == "fail" else user_ip_info["country"]
    if st.session_state["country"] not in utils.support_country:
        # print("uwu")
        st.session_state["country"] = "unknown"
        st.session_state["country"] = "Italy"
    if 'login' in st.session_state: 
        st.title(f'{utils.Hello[st.session_state["country"]]}:\t{st.session_state["login"]}.')
    else:
        st.title(f'{utils.Hello[st.session_state["country"]]}:\tGuest.')
    if user_ip_info['status'] == "success":
        st.write(f'Your country: {user_ip_info["country"]}')
    st.text(f'{utils.IPfrom[st.session_state["country"]]} {user_ip}')
    st.session_state["language"] = utils.country_to_language(st.session_state["country"])
    if first_reload and  st.session_state["country"] != "unknown":
        st.rerun()
    newPath = "./image/{}".format(st.session_state["country"])
    if not os.path.exists(newPath):
        os.makedirs(newPath)
    filePath = "./image/{}".format(st.session_state['country'])
    files = os.listdir(filePath)
    if len(files) != 0:
        image_file = random.choice(files)
        # img = load_image(filePath+"/"+image_file)
        # print("uwu", img, "owo", image_file)
        set_background(filePath+"/"+image_file)

if __name__ == "__main__":
    main()

