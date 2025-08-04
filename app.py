import streamlit as st
from utils.navegação import init_page_state
from pages.upload import pagina_upload
from pages.categorizar import pagina_categorizar
from pages.dashboard import pagina_dashboard

st.set_page_config(page_title="Dashboard Financeiro", layout="wide")
st.title("💸 Painel de Controle Financeiro")

init_page_state()

if st.session_state.page == 1:
    pagina_upload()
elif st.session_state.page == 2:
    pagina_categorizar()
elif st.session_state.page == 3:
    pagina_dashboard()