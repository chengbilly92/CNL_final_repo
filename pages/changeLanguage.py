import streamlit as st
import utils

def main() -> None:
    utils.set_sidebar()
    st.title('Change password')
    language = st.radio("",[
        "auto", ":flag-us: English", ":flag-jp: 日本語", ":flag-tw: 繁體中文", ":flag-fr: Français"
    ])
    st.session_state['man_language'] = language

if __name__ == "__main__":
    main()