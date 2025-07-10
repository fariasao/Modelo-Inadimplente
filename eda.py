import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Etapa 4: Análise Exploratória dos Dados (EDA)
# O objetivo aqui é entender o que temos nos dados e ver se já conseguimos tirar alguma ideia inicial.

# Criar pasta para salvar gráficos (opcional)
os.makedirs("graficos_eda", exist_ok=True)

# Carregar as bases de dados
df_pagamentos = pd.read_csv("pagamentos_com_target.csv", parse_dates=["DATA_VENCIMENTO", "DATA_PAGAMENTO"])
df_cadastral = pd.read_csv("data/base_cadastral.csv", sep=";")
df_info = pd.read_csv("data/base_info.csv", sep=";")

# Ver informações gerais de cada base
print("Informações da base de pagamentos com target:")
print(df_pagamentos.info())
print("\n")

print("Informações da base cadastral:")
print(df_cadastral.info())
print("\n")

print("Informações da base info (mensal):")
print(df_info.info())
print("\n")

# Ver como está a distribuição da variável INADIMPLENTE
print("Distribuição da variável INADIMPLENTE (0 = pagou em dia, 1 = atrasou):")
print(df_pagamentos['INADIMPLENTE'].value_counts(normalize=True))

# Gerar gráfico simples da variável alvo
sns.countplot(data=df_pagamentos, x='INADIMPLENTE')
plt.title("Distribuição de Inadimplência")
plt.savefig("graficos_eda/target_distribuicao.png")
plt.close()

# Ver quantas colunas têm valores ausentes
print("\nValores ausentes nas bases:")
print("Pagamentos:\n", df_pagamentos.isnull().sum())
print("Cadastral:\n", df_cadastral.isnull().sum())
print("Info:\n", df_info.isnull().sum())

# Estatísticas básicas das colunas numéricas
print("\nEstatísticas - Pagamentos:")
print(df_pagamentos.describe())

print("\nEstatísticas - Info:")
print(df_info.describe())

# Ver correlação entre colunas numéricas da base de pagamentos
plt.figure(figsize=(10, 6))
sns.heatmap(df_pagamentos.corr(numeric_only=True), annot=True, cmap="Blues")
plt.title("Correlação entre Variáveis - Pagamentos")
plt.tight_layout()
plt.savefig("graficos_eda/correlacao_pagamentos.png")
plt.close()

print("EDA finalizada. Os gráficos estão na pasta 'graficos_eda/'. Você pode usar as observações para alimentar o arquivo eda_resultados.md.")
