# Treinamento do Modelo

treinamos alguns modelos de machine learning para prever a inadimplência dos clientes, usando a base `base_modelagem.csv`

---

## Separação dos dados

- Separamos os dados em duas partes:
  - **Treino** (80%): para ensinar o modelo
  - **Validação** (20%): para testar se ele está indo bem

---

## Modelos testados

Treinamos três modelos diferentes para comparar:

1. **Regressão Logística** — modelo simples e rápido - Quis começar com um modelo simples para ter uma base de comparação com os outros modelos
2. **Random Forest** — modelo em árvore com vários estimadores - é fácil de usar e costuma dar bons resultados com dados tabulares como os do case. Também ajuda a entender a importância das variáveis
3. **XGBoost** — modelo mais robusto e usado em competições - geralmente tem melhor desempenho. Por isso, quis testar e comparar com os outros dois modelos

---

## Avaliação

Usamos duas métricas para saber qual modelo está melhor:

- **AUC**: mede o quanto o modelo consegue separar os inadimplentes dos adimplentes (quanto mais perto de 1, melhor) - é uma métrica comum para problemas de classificação binária
- **LogLoss**: mede o quão boas são as probabilidades que o modelo gera (quanto menor, melhor) - O LogLoss mede se o modelo está confiante, mas errado

---

## Escolha do modelo final

- O XGBoost teve o melhor desempenho nas duas métricas principais.
- Como ele conseguiu prever bem quem tem risco de inadimplência e deu probabilidades confiáveis (LogLoss), escolhi esse modelo para seguir com as previsões
