import streamlit as st
import pandas as pd
from utils.navegação import next_page, prev_page

def pagina_categorizar():
    st.header("2️⃣ Categorize seus gastos")
    df = st.session_state.get("df", pd.DataFrame())

    if df.empty:
        st.error("Nenhum dado carregado.")
        st.button("⬅️ Voltar", on_click=prev_page)
    else:
        for i, row in df[df["Categoria"] == ""].head(10).iterrows():
            categoria = st.selectbox(
                f"{row['Data'].date()} | {row['Descrição']} (R$ {row['Valor']:.2f})",
                ["", "Transporte", "Saúde", "Lazer", "Mercado", "Outros", "Receita"],
                key=f"cat_{i}"
            )
            if categoria:
                df.at[i, "Categoria"] = categoria

        st.session_state.df = df
        st.write("Total de lançamentos:", len(df))
        st.write("Faltando categorizar:", (df["Categoria"] == "").sum())

        col1, col2 = st.columns(2)
        col1.button("⬅️ Voltar", on_click=prev_page)
        if (df["Categoria"] == "").sum() == 0:
            col2.button("➡️ Avançar para Análise", on_click=next_page)
        else:
            col2.warning("⚠️ Categorize todos os lançamentos para continuar.")