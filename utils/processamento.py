import pandas as pd

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