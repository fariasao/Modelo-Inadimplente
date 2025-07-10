import pandas as pd
from xgboost import XGBClassifier

# Geração das Previsões

# Carregar a base de teste
df_teste = pd.read_csv("data/base_pagamentos_teste.csv", sep=";", parse_dates=["DATA_VENCIMENTO", "DATA_EMISSAO_DOCUMENTO"])

# Carregar base_info e base_cadastral para enriquecer
df_info = pd.read_csv("data/base_info.csv", sep=";")
df_cadastral = pd.read_csv("data/base_cadastral.csv", sep=";")

# Juntar com info e cadastral
df_teste = df_teste.merge(df_info, on=["ID_CLIENTE", "SAFRA_REF"], how="left")
df_teste = df_teste.merge(df_cadastral, on="ID_CLIENTE", how="left")

# Criar os mesmos atributos usados no treino
df_teste["DIAS_EMISSAO_VENCIMENTO"] = (df_teste["DATA_VENCIMENTO"] - df_teste["DATA_EMISSAO_DOCUMENTO"]).dt.days
df_teste["VALOR_POR_DIA"] = df_teste["VALOR_A_PAGAR"] / (df_teste["DIAS_EMISSAO_VENCIMENTO"] + 1)

# Preencher valores ausentes
df_teste["NO_FUNCIONARIOS"] = df_teste["NO_FUNCIONARIOS"].fillna(0)
df_teste["RENDA_MES_ANTERIOR"] = df_teste["RENDA_MES_ANTERIOR"].fillna(df_teste["RENDA_MES_ANTERIOR"].median())
df_teste["SEGMENTO_INDUSTRIAL"] = df_teste["SEGMENTO_INDUSTRIAL"].fillna("NA")
df_teste["DOMINIO_EMAIL"] = df_teste["DOMINIO_EMAIL"].fillna("desconhecido")
df_teste["PORTE"] = df_teste["PORTE"].astype(str)

# Codificação (igual ao treino)
df_teste["PORTE_COD"] = df_teste["PORTE"].astype("category").cat.codes
df_teste["SEGMENTO_COD"] = df_teste["SEGMENTO_INDUSTRIAL"].astype("category").cat.codes
df_teste["EMAIL_COD"] = df_teste["DOMINIO_EMAIL"].astype("category").cat.codes

# Criar DIAS_ATRASO como 0 apenas para manter compatibilidade com os dados de treino
df_teste["DIAS_ATRASO"] = 0

# Selecionar colunas para previsão (mesmas usadas no X_train)
colunas_modelo = [
    "VALOR_A_PAGAR", "TAXA", "RENDA_MES_ANTERIOR", "NO_FUNCIONARIOS",
    "DIAS_ATRASO", "DIAS_EMISSAO_VENCIMENTO", "VALOR_POR_DIA", 
    "PORTE_COD", "SEGMENTO_COD", "EMAIL_COD"
]

X_teste = df_teste[colunas_modelo].fillna(0)
X_teste.replace([float('inf'), float('-inf')], 0, inplace=True)

# Treinar novamente o modelo com os dados
df_modelagem = pd.read_csv("base_modelagem.csv")
X = df_modelagem.drop(columns=["INADIMPLENTE", "ID_CLIENTE", "SAFRA_REF"]).fillna(0)
X.replace([float("inf"), float("-inf")], 0, inplace=True)
y = df_modelagem["INADIMPLENTE"]

xgb_model = XGBClassifier(n_estimators=100, use_label_encoder=False, eval_metric="logloss", random_state=42)
xgb_model.fit(X, y)

# Fazer as previsões
df_teste["PROBABILIDADE_INADIMPLENCIA"] = xgb_model.predict_proba(X_teste)[:, 1]

# Gerar submissão
df_submissao = df_teste[["ID_CLIENTE", "SAFRA_REF", "PROBABILIDADE_INADIMPLENCIA"]]
df_submissao.to_csv("submissao_case.csv", index=False)

print("Arquivo 'submissao_case.csv' gerado com sucesso!")
