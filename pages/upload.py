import streamlit as st
import sqlite3
import traceback
import utils
import pandas as pd
from PIL import Image
import os

@st.cache_data
def load_image(image_file):
    img = Image.open(image_file)
    return img
def main()-> None:
    utils.set_sidebar()
    if 'tologin' in st.session_state:
        del st.session_state['tologin']
        del st.session_state['login']
        st.switch_page('index.py')
    st.text("You've now logged in as {}., located in {}".format(st.session_state.login, st.session_state.country))
    st.title('Share your country with people!')
    image_file = st.file_uploader("Upload An Image",type=['png','jpeg','jpg'])
    if image_file is not None:
        file_details = {"FileName":image_file.name,"FileType":image_file.type}
        st.write(file_details)
        img = load_image(image_file)
        st.image(img)
        newPath = "./image/{}".format(st.session_state['country'])
        if not os.path.exists(newPath):
            os.makedirs(newPath)
        with open(os.path.join(newPath,image_file.name), "wb") as f: 
          f.write(image_file.getbuffer())
        st.success("Saved File")

    # st.button('change', on_click=lambda: change_password(st.session_state.login, oldPassword, password))

if __name__ == "__main__":
    main()



