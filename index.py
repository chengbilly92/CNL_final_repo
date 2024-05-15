import streamlit as st
from streamlit import runtime
from streamlit.runtime.scriptrunner import get_script_run_ctx

def get_remote_ip() -> str:
    ctx = get_script_run_ctx()
    if not ctx: return None
    session_info = runtime.get_instance().get_client(ctx.session_id)
    if not session_info: return None
    return session_info.request.remote_ip

if 'login' in st.session_state:
    st.title(f'Hello:\t{st.session_state["login"]}.')
else:
    st.title(f'Hello:\tGuest.')

st.text(f'Your ip address: {get_remote_ip()}')

