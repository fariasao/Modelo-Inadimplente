import pandas as pd
import numpy as np
import os

# Pré-processamento

# Carregar as bases
df_pagamentos = pd.read_csv("pagamentos_com_target.csv", parse_dates=["DATA_VENCIMENTO", "DATA_PAGAMENTO"])
df_cadastral = pd.read_csv("data/base_cadastral.csv", sep=";")
df_info = pd.read_csv("data/base_info.csv", sep=";")

# Juntar as bases usando ID_CLIENTE e SAFRA_REF quando possível
df_merged = df_pagamentos.merge(df_info, on=["ID_CLIENTE", "SAFRA_REF"], how="left")
df_merged = df_merged.merge(df_cadastral, on="ID_CLIENTE", how="left")

# Tratamento de valores ausentes
df_merged["NO_FUNCIONARIOS"] = df_merged["NO_FUNCIONARIOS"].fillna(0)
df_merged["RENDA_MES_ANTERIOR"] = df_merged["RENDA_MES_ANTERIOR"].fillna(df_merged["RENDA_MES_ANTERIOR"].median())
df_merged["SEGMENTO_INDUSTRIAL"] = df_merged["SEGMENTO_INDUSTRIAL"].fillna("NA")
df_merged["DOMINIO_EMAIL"] = df_merged["DOMINIO_EMAIL"].fillna("desconhecido")

# Engenharia de Atributos
df_merged["DIAS_EMISSAO_VENCIMENTO"] = (pd.to_datetime(df_merged["DATA_VENCIMENTO"]) - pd.to_datetime(df_merged["DATA_EMISSAO_DOCUMENTO"])).dt.days
df_merged["VALOR_POR_DIA"] = df_merged["VALOR_A_PAGAR"] / (df_merged["DIAS_EMISSAO_VENCIMENTO"] + 1)

# categorias em números
df_merged["PORTE"] = df_merged["PORTE"].astype(str)
df_merged["PORTE_COD"] = df_merged["PORTE"].astype("category").cat.codes
df_merged["SEGMENTO_COD"] = df_merged["SEGMENTO_INDUSTRIAL"].astype("category").cat.codes
df_merged["EMAIL_COD"] = df_merged["DOMINIO_EMAIL"].astype("category").cat.codes

# Selecionar apenas colunas úteis para o modelo
colunas_modelo = [
    "ID_CLIENTE", "SAFRA_REF", "VALOR_A_PAGAR", "TAXA",
    "RENDA_MES_ANTERIOR", "NO_FUNCIONARIOS", "DIAS_ATRASO", "DIAS_EMISSAO_VENCIMENTO",
    "VALOR_POR_DIA", "PORTE_COD", "SEGMENTO_COD", "EMAIL_COD", "INADIMPLENTE"
]

df_modelagem = df_merged[colunas_modelo]

# Salvar a base pronta para modelagem
df_modelagem.to_csv("base_modelagem.csv", index=False)
print("Arquivo base_modelagem.csv salvo com sucesso!")
