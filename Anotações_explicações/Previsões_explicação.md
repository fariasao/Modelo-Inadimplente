# Previsões

## Objetivo
Aplicar o modelo final treinado (XGBoost) sobre a base de teste (`base_pagamentos_teste.csv`) para estimar a **probabilidade de inadimplência** de cada cliente. O resultado é exportado em um arquivo `submissao_case.csv`

---

1. **Leitura da base de teste**  
   A base `base_pagamentos_teste.csv` foi carregada com as colunas de data tratadas corretamente

2. **Enriquecimento da base de teste**  
   Foram feitas junções com:
   - `base_info.csv`: histórico financeiro por cliente e safra
   - `base_cadastral.csv`: informações cadastrais do cliente

3. **Criação das mesmas variáveisdo treino**  
   Recriamos as seguintes features:
   - `DIAS_EMISSAO_VENCIMENTO`: diferença entre vencimento e emissão do documento
   - `VALOR_POR_DIA`: valor a pagar dividido pelos dias de vencimento
   - `DIAS_ATRASO`: como a base de teste não possui essa informação, foi preenchida com zero, apenas para manter o formato esperado pelo modelo

4. **Tratamento de valores ausentes**
   - Preenchimento de `NaN` com 0 ou valores padrão para garantir consistência.
   - Codificação de variáveis categóricas (`PORTE_COD`, `SEGMENTO_COD`, `EMAIL_COD`)

5. **Padronização de colunas para previsão**  
   As colunas utilizadas na previsão foram as mesmas da base de treino:

   colunas_modelo = [
       "VALOR_A_PAGAR", "TAXA", "RENDA_MES_ANTERIOR", "NO_FUNCIONARIOS",
       "DIAS_ATRASO", "DIAS_EMISSAO_VENCIMENTO", "VALOR_POR_DIA",
       "PORTE_COD", "SEGMENTO_COD", "EMAIL_COD"
   ]

6. **Re-treinamento do modelo com 100% da base de modelagem**  
   Para garantir que o modelo aproveite todos os dados possíveis, o XGBoost foi treinado novamente com toda a base de modelagem (`base_modelagem.csv`).

7. **Aplicação do modelo e geração das previsões**
   As probabilidades de inadimplência foram geradas com `predict_proba()` e adicionadas à base

8. **Criação do arquivo de submissão**
   Geramos o arquivo `submissao_case.csv` com as colunas:

   - `ID_CLIENTE`
   - `SAFRA_REF`
   - `PROBABILIDADE_INADIMPLENCIA`

## Justificativas
- Durante o treino final do XGBoost, aplicamos o mesmo tratamento da etapa anterior, substituindo valores infinitos por zero. Isso garante que o modelo aceite a base sem erros, mantendo a consistência do pipeline.
- Garantimos **consistência** entre os dados de treino e de teste.
- Reutilizamos o mesmo pipeline de pré-processamento, assegurando reprodutibilidade.
- O re-treinamento com todos os dados disponíveis permite que o modelo tenha **maior capacidade de generalização**
