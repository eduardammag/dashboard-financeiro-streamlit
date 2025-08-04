import streamlit as st

def init_page_state():
    if "page" not in st.session_state:
        st.session_state.page = 1

def next_page():
    st.session_state.page += 1

def prev_page():
    st.session_state.page -= 1