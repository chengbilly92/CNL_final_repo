import streamlit as st
import utils
from PIL import Image
import os

@st.cache_data
def load_image(image_file):
    img = Image.open(image_file)
    return img
def main()-> None:
    utils.set_sidebar()
    st.text("{}{}., located in {}".format(utils.CurrentLogin[st.session_state.country], st.session_state.login, st.session_state.country))
    st.title(utils.Share[st.session_state.country])
    image_file = st.file_uploader("Upload An Image",type=['png'])
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

if __name__ == "__main__":
    main()



