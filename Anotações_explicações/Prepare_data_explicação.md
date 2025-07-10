# Pré-processamento

criamos novas colunas que podem ajudar o modelo a aprender melhor

---

## Limpeza e Preenchimento de Dados

- Algumas colunas tinham valores vazios (nulos), como número de funcionários e segmento industrial.
- Preenchi os nulos com:
  - `0` para número de funcionários
  - `mediana` para renda
  - `"NA"` ou `"desconhecido"` para colunas de texto
- Isso evita que esses campos vazios

---

## Engenharia de Atributos

Criei algumas colunas novas que podem ser úteis para o modelo prever inadimplência:

- `DIAS_EMISSAO_VENCIMENTO`: dias entre a emissão e o vencimento da cobrança
- `VALOR_POR_DIA`: valor da cobrança dividido pelos dias da cobrança

---

## Transformação de Texto em Número

O modelo não entende texto. Então transformei algumas colunas em numeros

- `PORTE`, `SEGMENTO_INDUSTRIAL` e `DOMINIO_EMAIL` viraram códigos numéricos usando Label Encoding

---

## Base Final

Depois de tudo isso, selecionei as colunas mais importantes e salvei a base final como:

**`base_modelagem.csv`**

Essa base está pronta para ser usada no treinamento dos modelos.
