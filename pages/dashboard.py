import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from utils.navegação import prev_page

def pagina_dashboard():
    st.header("3️⃣ Dashboard Financeiro")
    df = st.session_state.get("df", pd.DataFrame())

    if df.empty:
        st.error("Nenhum dado carregado.")
        st.button("⬅️ Voltar", on_click=prev_page)
    else:
        st.subheader("📄 Lançamentos")
        st.dataframe(df[["Data", "Descrição", "Valor", "Categoria"]], use_container_width=True)

        st.sidebar.header("🎯 Filtros")
        categorias = st.sidebar.multiselect("Filtrar por categoria", df["Categoria"].unique(), default=list(df["Categoria"].unique()))
        df_filtrado = df[df["Categoria"].isin(categorias)]

        st.subheader("📌 Total por Categoria")
        categoria_sum = df_filtrado.groupby("Categoria")["Valor"].sum().reset_index()

        fig1, ax1 = plt.subplots()
        sns.barplot(data=categoria_sum, x="Categoria", y="Valor", ax=ax1)
        st.pyplot(fig1)

        st.subheader("📈 Evolução Mensal")
        df_filtrado["Ano-Mês"] = df_filtrado["Data"].dt.to_period("M").astype(str)
        mensal = df_filtrado.groupby("Ano-Mês")["Valor"].sum().reset_index()

        fig2, ax2 = plt.subplots()
        sns.lineplot(data=mensal, x="Ano-Mês", y="Valor", marker="o", ax=ax2)
        ax2.tick_params(axis='x', rotation=45)
        st.pyplot(fig2)

        st.button("⬅️ Voltar para Categorizar", on_click=prev_page)