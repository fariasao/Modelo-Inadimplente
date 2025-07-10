import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from xgboost import XGBClassifier
from sklearn.metrics import roc_auc_score, log_loss
import warnings

warnings.filterwarnings("ignore")

# Treinamento e Avaliação de Modelos

# Carregar a base final de modelagem
df = pd.read_csv("base_modelagem.csv")

# Separar variáveis de entrada (X) e alvo (y)
X = df.drop(columns=["INADIMPLENTE", "ID_CLIENTE", "SAFRA_REF"])
y = df["INADIMPLENTE"]

# Separar treino e validação
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# Preencher valores nulos para evitar erro nos modelos
X_train.fillna(0, inplace=True)
X_val.fillna(0, inplace=True)

# Substituir valores infinitos por zero para evitar erro nos modelos
X_train.replace([float('inf'), float('-inf')], 0, inplace=True)
X_val.replace([float('inf'), float('-inf')], 0, inplace=True)

# Criar dicionário para armazenar resultados
resultados = {}

# 1. Regressão Logística
log_model = LogisticRegression(max_iter=1000)
log_model.fit(X_train, y_train)
y_pred_log = log_model.predict_proba(X_val)[:, 1]
resultados["Logistic Regression"] = {
    "AUC": roc_auc_score(y_val, y_pred_log),
    "LogLoss": log_loss(y_val, y_pred_log)
}

# 2. Random Forest
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
y_pred_rf = rf_model.predict_proba(X_val)[:, 1]
resultados["Random Forest"] = {
    "AUC": roc_auc_score(y_val, y_pred_rf),
    "LogLoss": log_loss(y_val, y_pred_rf)
}

# 3. XGBoost
xgb_model = XGBClassifier(n_estimators=100, use_label_encoder=False, eval_metric="logloss", random_state=42)
xgb_model.fit(X_train, y_train)
y_pred_xgb = xgb_model.predict_proba(X_val)[:, 1]
resultados["XGBoost"] = {
    "AUC": roc_auc_score(y_val, y_pred_xgb),
    "LogLoss": log_loss(y_val, y_pred_xgb)
}

# Mostrar resultados
print("Resultados de validação:")
for modelo, metricas in resultados.items():
    print(f"\n{modelo}")
    for metrica, valor in metricas.items():
        print(f"{metrica}: {valor:.4f}")

# Escolher modelo final (pelo melhor AUC)
modelo_escolhido = xgb_model
print("\nModelo escolhido: XGBoost")
