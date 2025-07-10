# Resultados da An�lise Explorat�ria (EDA)

Esta an�lise � uma vis�o inicial sobre os dados dispon�veis no case. O objetivo aqui foi entender o que temos padr�es ou problemas.

---

## Vari�vel alvo: `INADIMPLENTE`

- A maioria dos clientes n�o est� inadimplente, a classe 0 (pagou em dia) � muito mais frequente do que a classe 1.
- Isso mostra um **desbalanceamento**, e talvez tenha que tratar isso.

---

## Valores ausentes

- Algumas colunas t�m **valores nulos**, como `SEGMENTO_INDUSTRIAL`, `DOMINIO_EMAIL` e `NO_FUNCIONARIOS`.
- Isso pode afetar os modelos e precisa ser tratado.

---

## Vari�veis num�ricas

- `VALOR_A_PAGAR` e `TAXA` s�o colunas que podem ter rela��o com a inadimpl�ncia.
- Ainda n�o fiz testes, mas acredito que **valores maiores podem aumentar a chance de atraso**.
- `RENDA_MES_ANTERIOR` e `NO_FUNCIONARIOS` s�o colunas relevantes.

---

## Observa��es gerais

- A base parece limpa, com datas bem formatadas.
- Os dados s�o mensais (`SAFRA_REF`) e o relacionamento entre as bases est� funcionando.
- Alguns gr�ficos foram salvos na pasta `graficos_eda/`.
