import pandas as pd
import matplotlib.pyplot as plt

# Resultados salvos da etapa de modelagem
resultados = {
    "Logistic Regression": {"AUC": 0.9999, "LogLoss": 0.0073},
    "Random Forest": {"AUC": 1.0000, "LogLoss": 0.0007},
    "XGBoost": {"AUC": 1.0000, "LogLoss": 0.0000}
}

# Transformar em DataFrame
df_resultados = pd.DataFrame(resultados).T

# Mostrar tabela no console
print("\nResultados comparativos entre modelos:")
print(df_resultados)

# Gerar gráfico de barras
df_resultados.plot(kind="bar", figsize=(10, 5), title="Comparação de Modelos (AUC e LogLoss)")
plt.xticks(rotation=0)
plt.ylabel("Score")
plt.grid(True)
plt.tight_layout()
plt.show()
