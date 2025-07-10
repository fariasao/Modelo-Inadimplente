# Resultados da Análise Exploratória (EDA)

Esta análise é uma visão inicial sobre os dados disponíveis no case. O objetivo aqui foi entender o que temos padrões ou problemas.

---

## Variável alvo: `INADIMPLENTE`

- A maioria dos clientes não está inadimplente, a classe 0 (pagou em dia) é muito mais frequente do que a classe 1.
- Isso mostra um **desbalanceamento**, e talvez tenha que tratar isso.

---

## Valores ausentes

- Algumas colunas têm **valores nulos**, como `SEGMENTO_INDUSTRIAL`, `DOMINIO_EMAIL` e `NO_FUNCIONARIOS`.
- Isso pode afetar os modelos e precisa ser tratado.

---

## Variáveis numéricas

- `VALOR_A_PAGAR` e `TAXA` são colunas que podem ter relação com a inadimplência.
- Ainda não fiz testes, mas acredito que **valores maiores podem aumentar a chance de atraso**.
- `RENDA_MES_ANTERIOR` e `NO_FUNCIONARIOS` são colunas relevantes.

---

## Observações gerais

- A base parece limpa, com datas bem formatadas.
- Os dados são mensais (`SAFRA_REF`) e o relacionamento entre as bases está funcionando.
- Alguns gráficos foram salvos na pasta `graficos_eda/`.
