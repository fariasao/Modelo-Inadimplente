import pandas as pd

# Construção da Variável Target

# Carregar a base de pagamentos de desenvolvimento
df = pd.read_csv("data/base_pagamentos_desenvolvimento.csv", sep=";", parse_dates=["DATA_PAGAMENTO", "DATA_VENCIMENTO"])

# Calcular o atraso em dias entre o pagamento e o vencimento
df["DIAS_ATRASO"] = (df["DATA_PAGAMENTO"] - df["DATA_VENCIMENTO"]).dt.days

# Criar a variável target:
# INADIMPLENTE = 1 se atraso for igual ou maior que 5 dias, senão 0
df["INADIMPLENTE"] = (df["DIAS_ATRASO"] >= 5).astype(int)

# Visualizar algumas linhas
print(df[["ID_CLIENTE", "SAFRA_REF", "DATA_VENCIMENTO", "DATA_PAGAMENTO", "DIAS_ATRASO", "INADIMPLENTE"]].head())

# Salvar a base com a variável target criada
df.to_csv("pagamentos_com_target.csv", index=False)
print("Arquivo pagamentos_com_target.csv salvo com sucesso!")
