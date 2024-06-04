import streamlit as st
import utils

def on_change() -> None:
    st.session_state['clanguage'] = True

def main() -> None:
    utils.set_sidebar()
    st.title(utils.ChangeLanguage[st.session_state['country']])
    language = st.radio("",[
        "auto", ":flag-us: English", ":flag-jp: 日本語", 
        ":flag-tw: 繁體中文",
    ], on_change= on_change)
    match language:
        case "auto":
            st.session_state["country"] = "unknown"
        case ":flag-us: English":
            st.session_state["country"] = "unknown"
        case ":flag-jp: 日本語":
            st.session_state["country"] = "Japan"
        case ":flag-tw: 繁體中文":
            st.session_state["country"] = "Taiwan"
            
    if 'clanguage' in st.session_state:
        del st.session_state['clanguage']
        st.rerun()
        
if __name__ == "__main__":
    main()
