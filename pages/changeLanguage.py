import streamlit as st
import utils

def main() -> None:
    utils.set_sidebar()
    st.title(utils.ChangeLanguage[st.session_state['country']])
    language = st.radio("",[
        "auto", ":flag-us: English", ":flag-jp: 日本語", 
        ":flag-tw: 繁體中文",
    ])
    match language:
        case "auto":
            st.session_state["country"] = "unknown"
        case ":flag-us: English":
            st.session_state["country"] = "unknown"
        case ":flag-jp: 日本語":
            st.session_state["country"] = "Japan"
        case ":flag-tw: 繁體中文":
            st.session_state["country"] = "Taiwan"

    # st.switch_page('index.py')
    # st.rerun()
    utils.set_sidebar()

if __name__ == "__main__":
    main()
