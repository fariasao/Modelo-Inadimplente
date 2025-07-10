# 🧠 Case Datarisk - Analista de Dados Júnior 2025

Este projeto tem como objetivo desenvolver um modelo preditivo para estimar a **probabilidade de inadimplência** de clientes com base em dados cadastrais e históricos de pagamento. O desafio foi proposto pela Datarisk como parte do processo seletivo de Cientista de Dados Júnior.

---

## 🎯 Objetivo

Prever, para cada cliente e safra (mês de referência), a probabilidade de que ele se torne inadimplente, utilizando modelos supervisionados e dados fornecidos pela empresa.

---

## 🧩 Etapas do Projeto

1. **Entendimento do Problema e Planejamento**  
   Leitura do desafio, compreensão das bases e definição do pipeline.

2. **Preparação do Ambiente**  
   Definição da versão do Python e bibliotecas necessárias (disponíveis em `requirements.txt`).

3. **Construção da Variável Target (`INADIMPLENTE`)**  
   Criada com base na regra: pagamento com 5 dias ou mais de atraso.

4. **Análise Exploratória dos Dados (EDA)**  
   Visualização de distribuições, identificação de padrões, valores ausentes e correlações.

5. **Pré-processamento e Engenharia de Atributos**  
   - Criação de variáveis como `VALOR_POR_DIA`, `DIAS_EMISSAO_VENCIMENTO`
   - Codificação de variáveis categóricas (porte, email, segmento)
   - Tratamento de nulos e normalização

6. **Modelagem Preditiva**  
   Teste dos modelos:
   - Regressão Logística
   - Random Forest
   - XGBoost (modelo final escolhido)

   Avaliação com métricas:
   - **AUC** (quanto melhor, mais próximo de 1)
   - **LogLoss** (quanto menor, melhor)

7. **Geração das Previsões**  
   Aplicação do modelo final sobre a base de teste e geração do arquivo `submissao_case.csv` com:
   - `ID_CLIENTE`
   - `SAFRA_REF`
   - `PROBABILIDADE_INADIMPLENCIA`

8. **Documentação e Reprodutibilidade**  
   Todos os passos do projeto foram documentados com scripts `.py` e arquivos `.md`.

---

## 📁 Estrutura dos Arquivos

| Arquivo/Pasta                       | Descrição                                                                 |
|------------------------------------|---------------------------------------------------------------------------|
| `requirements.txt`                 | Bibliotecas utilizadas com versões recomendadas                          |
| `pagamentos_com_target.csv`        | Base com variável INADIMPLENTE gerada                                    |
| `base_modelagem.csv`               | Base final com features para modelagem                                   |
| `submissao_case.csv`               | Resultado final da predição para submissão                               |
| `prepare_data.py`                  | Script de pré-processamento                                               |
| `modelagem.py`                     | Script de treinamento e validação dos modelos                            |
| `previsoes.py`                     | Script para aplicar o modelo na base de teste                            |
| `eda.py`                           | Script com análise exploratória                                           |
| `README.md`                        | Documentação geral do projeto                                             |
| `Anotações_expliações/*.md`        | Explicações por etapa (EDA, modelagem, previsão etc.)                    |

---

## ▶️ Como Rodar o Projeto

1. **Instale os pacotes**:

```bash
pip install -r requirements.txt
```

2. **Execute os scripts na seguinte ordem**:

```bash
python construcao_target.py
python eda.py
python prepare_data.py
python modelagem.py
python previsoes.py
```

> Os arquivos de entrada estão na pasta `data/`. O arquivo final `submissao_case.csv` será gerado na raiz do projeto.

---

## ✅ Observações

- A variável `INADIMPLENTE` foi criada com base em 5 ou mais dias de atraso no pagamento.
- O modelo **XGBoost** apresentou os melhores resultados em AUC e LogLoss, sendo o escolhido.
- O projeto é 100% reprodutível e organizado em etapas.

---

## 👤 Autor

Desenvolvido por Enzo Farias Alves Oliveira — Analista de Dados.
