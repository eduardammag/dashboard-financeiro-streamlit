import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Dashboard Financeiro", layout="wide")

# === Funções auxiliares ===
def carregar_e_processar(files):
    dfs = []
    for file in files:
        df = pd.read_csv(file)
        if {"date", "title", "amount"}.issubset(df.columns):
            df["Data"] = pd.to_datetime(df["date"])
            df["Dia"] = df["Data"].dt.day
            df["Mês"] = df["Data"].dt.month
            df["Ano"] = df["Data"].dt.year
            df["Descrição"] = df["title"]
            df["Valor"] = df["amount"]
            df["Categoria"] = ""  # iniciar categoria vazia
            dfs.append(df)
    if dfs:
        return pd.concat(dfs, ignore_index=True)
    return pd.DataFrame(columns=["Data", "Descrição", "Valor", "Categoria", "Dia", "Mês", "Ano"])

# === Controle de página ===
if "page" not in st.session_state:
    st.session_state.page = 1

def next_page():
    st.session_state.page += 1

def prev_page():
    st.session_state.page -= 1

st.title("💸 Painel de Controle Financeiro")

# === Página 1: Upload ===
if st.session_state.page == 1:
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

# === Página 2: Categorizar ===
elif st.session_state.page == 2:
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

# === Página 3: Dashboard ===
elif st.session_state.page == 3:
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

        # Total por categoria
        st.subheader("📌 Total por Categoria")
        categoria_sum = df_filtrado.groupby("Categoria")["Valor"].sum().reset_index()

        fig1, ax1 = plt.subplots()
        sns.barplot(data=categoria_sum, x="Categoria", y="Valor", ax=ax1)
        st.pyplot(fig1)

        # Evolução mensal
        st.subheader("📈 Evolução Mensal")
        df_filtrado["Ano-Mês"] = df_filtrado["Data"].dt.to_period("M").astype(str)
        mensal = df_filtrado.groupby("Ano-Mês")["Valor"].sum().reset_index()

        fig2, ax2 = plt.subplots()
        sns.lineplot(data=mensal, x="Ano-Mês", y="Valor", marker="o", ax=ax2)
        ax2.tick_params(axis='x', rotation=45)
        st.pyplot(fig2)

        # Navegação
        st.button("⬅️ Voltar para Categorizar", on_click=prev_page)

                

