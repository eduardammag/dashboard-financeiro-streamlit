import streamlit as st
from utils.processamento import carregar_e_processar
from utils.navegação import next_page

def pagina_upload():
    st.header("1️⃣ Envio dos Arquivos")
    arquivos = st.file_uploader("Carregue um ou mais arquivos .csv", type=["csv"], accept_multiple_files=True)

    if arquivos:
        df_total = carregar_e_processar(arquivos)
        st.session_state.df = df_total
        st.success(f"{len(arquivos)} arquivos carregados com sucesso.")
        if not df_total.empty:
            st.button("➡️ Avançar para Categorizar", on_click=next_page)
    else:
        st.info("Envie ao menos um arquivo com colunas: `date`, `title`, `amount`.")