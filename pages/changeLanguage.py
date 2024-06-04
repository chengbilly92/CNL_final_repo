import streamlit as st
import utils

def main() -> None:
    utils.set_sidebar()
    st.title('Change password')
    language = st.radio("",[
        "auto", ":flag-us: English", ":flag-jp: 日本語", 
        ":flag-tw: 繁體中文",
    ])
    match language:
        case "auto":
            st.session_state['man_language'] = "unknown"
        case ":flag-us: English":
            st.session_state['man_language'] = "unknown"
        case ":flag-jp: 日本語":
            st.session_state['man_language'] = "Japan"
        case ":flag-tw: 繁體中文":
            st.session_state['man_language'] = "Taiwan"


if __name__ == "__main__":
    main()