# Resultados da An�lise Explorat�ria (EDA)

Esta analise é uma visão inicial sobre os dados dispon�veis no case. O objetivo aqui foi entender o que temos padrões ou problemas.

---

## Variavel alvo: `INADIMPLENTE`

- A maioria dos clientes não está inadimplente, a classe 0 (pagou em dia) muito mais frequente do que a classe 1.
- Isso mostra um **desbalanceamento**, e talvez tenha que tratar isso.

---

## Valores ausentes

- Algumas colunas tem **valores nulos**, como `SEGMENTO_INDUSTRIAL`, `DOMINIO_EMAIL` e `NO_FUNCIONARIOS`.
- Isso pode afetar os modelos e precisa ser tratado.

---

## Variaveis numericas

- `VALOR_A_PAGAR` e `TAXA` são colunas que podem ter relaçãoo com a inadimplencia.
- Ainda não fiz testes, mas acredito que **valores maiores podem aumentar a chance de atraso**.
- `RENDA_MES_ANTERIOR` e `NO_FUNCIONARIOS` são colunas relevantes.

---

## Observa��es gerais

- A base parece limpa, com datas bem formatadas.
- Os dados são mensais (`SAFRA_REF`) e o relacionamento entre as bases esta funcionando.
- Alguns graficos foram salvos na pasta `graficos_eda/`.
