# 📊 E-commerce Analytics: Insights Estratégicos com o Dataset Olist

![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow)
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Pandas](https://img.shields.io/badge/Library-Pandas-brightgreen)

## 📌 Visão Geral do Projeto
Este projeto consiste em uma análise fim-a-fim do ecossistema de e-commerce brasileiro utilizando dados reais da **Olist**. O objetivo é transformar dados brutos em inteligência de negócio, focando em otimização logística, saúde financeira e segmentação de clientes para suporte à tomada de decisão.


## 🎯 Perguntas de Negócio
A análise foi estruturada para responder aos seguintes desafios:
* **Logística:** Qual o Lead Time médio por estado e como o atraso impacta o NPS?
* **Vendas:** Qual a evolução do **GMV** e do **Ticket Médio** mensal? Existe sazonalidade clara?
* **Marketing (RFM):** Quem são os clientes "Campeões" e quais estão em risco de churn?
* **Pagamentos:** Como a escolha do método de pagamento e o parcelamento influenciam o valor final da compra?

## 🛠️ Tecnologias e Ferramentas
* **Python (Pandas/NumPy):** Limpeza, tratamento de tipos (Data/ZipCode) e manipulação de DataFrames.
* **Matplotlib & Seaborn:** Criação de visualizações estatísticas e dashboards de apoio.


## 🗂️ Estrutura do Dataset
O projeto utiliza um modelo relacional (Star Schema) com as seguintes tabelas principais:
1.  `olist_orders`: O "coração" com status e timestamps.
2.  `olist_order_items`: Itens, preços e custos de frete.
3.  `olist_customers`: Identificação única e localização dos compradores.
4.  `olist_products`: Categorias e atributos dos produtos.
5.  `olist_order_payments`: Métodos de pagamento e parcelamento.
6.  `olist_sellers` & `olist_geolocation`: Dados de origem e coordenadas.


## ✒️ Autor
**Gabriel Duarte** - Cientista de Dados
* [LinkedIn](https://www.linkedin.com/in/djgabriel93/)

## 📂 Organização do projeto

```
├── .env               <- Arquivo de variáveis de ambiente (não versionar)
├── .gitignore         <- Arquivos e diretórios a serem ignorados pelo Git
├── ambiente.yml       <- O arquivo de requisitos para reproduzir o ambiente de análise
├── LICENSE            <- Licença de código aberto se uma for escolhida
├── README.md          <- README principal para desenvolvedores que usam este projeto.
|
├── dados              <- Arquivos de dados para o projeto.
|
├── modelos            <- Modelos treinados e serializados, previsões de modelos ou resumos de modelos
|
├── notebooks          <- Cadernos Jupyter. A convenção de nomenclatura é um número (para ordenação),
│                         as iniciais do criador e uma descrição curta separada por `-`, por exemplo
│                         `01-fb-exploracao-inicial-de-dados`.
│
|   └──src             <- Código-fonte para uso neste projeto.
|      │
|      ├── __init__.py  <- Torna um módulo Python
|      ├── config.py    <- Configurações básicas do projeto
|      └── graficos.py  <- Scripts para criar visualizações exploratórias e orientadas a resultados
|
├── referencias        <- Dicionários de dados, manuais e todos os outros materiais explicativos.
|
├── relatorios         <- Análises geradas em HTML, PDF, LaTeX, etc.
│   └── imagens        <- Gráficos e figuras gerados para serem usados em relatórios
```
