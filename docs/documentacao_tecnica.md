# Documentação Técnica – Totem Inteligente FlexMedia

## 1. Visão Geral do Sistema

O sistema desenvolvido consiste em um protótipo de Totem Inteligente capaz de registrar interações de usuários em ambientes como shopping centers e gerar insights a partir desses dados.

A solução integra coleta de dados, armazenamento, análise e aplicação de Machine Learning para gerar previsões sobre o comportamento dos usuários.

---

## 2. Pipeline de Dados

O sistema segue o seguinte fluxo de dados:

Usuário → Totem → Sensor de interação → Script Python → Banco de dados → Análise de dados → Machine Learning → Dashboard

Cada etapa do pipeline é responsável por processar e transformar os dados até que eles possam gerar insights úteis para análise de comportamento.

---

## 3. Coleta de Dados

A coleta de dados é realizada por um sensor simulado desenvolvido em Python.

O script gera interações simuladas contendo:

* categoria escolhida pelo usuário
* preferência
* tempo de interação
* recomendação sugerida
* aceitação da recomendação

Essas informações representam o comportamento de visitantes utilizando o totem.

---

## 4. Armazenamento de Dados

Os dados são armazenados em um banco de dados SQLite.

Tabela principal:

interacoes

Campos armazenados:

* id
* timestamp
* categoria
* preferencia
* tempo_interacao
* recomendacao
* aceitou_recomendacao

---

## 5. Análise de Dados

Utilizando a biblioteca Pandas, os dados são analisados para gerar métricas de uso, incluindo:

* total de interações
* categorias mais buscadas
* taxa de aceitação das recomendações

Essas métricas ajudam a compreender o comportamento dos visitantes.

---

## 6. Modelo de Machine Learning

Foi implementado um modelo de classificação utilizando o algoritmo Random Forest.

O objetivo do modelo é prever se uma recomendação feita pelo sistema será aceita ou não pelo usuário.

Variáveis utilizadas no modelo:

* categoria
* preferência
* tempo de interação
* recomendação sugerida

O modelo foi treinado utilizando divisão de treino e teste.

Resultado obtido:

Acurácia aproximada: 52%

---

## 7. Visualização de Dados

Para visualização das métricas foi desenvolvido um dashboard interativo utilizando Streamlit.

O dashboard apresenta:

* total de interações
* taxa de aceitação
* gráficos de categorias
* gráficos de comportamento dos usuários

Esse painel permite acompanhar o desempenho do sistema em tempo real.

---

## 8. Tecnologias Utilizadas

Python
SQLite
Pandas
Scikit-Learn
Streamlit
Matplotlib
