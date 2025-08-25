# 🛒 Projeto ETL e Dashboard – Online Sales UK

[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)](https://www.python.org/)
[![Power BI](https://img.shields.io/badge/PowerBI-Data%20Visualization-yellow?logo=microsoft-power-bi)](https://powerbi.microsoft.com/)
[![SQL Server](https://img.shields.io/badge/SQL%20Server-Database-red?logo=microsoftsqlserver)](https://www.microsoft.com/en-us/sql-server)

## 📖 Contexto
Este projeto utiliza o dataset **Online Retail** disponível no Kaggle, mas com fonte direa do [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Online+Retail).  
O dataset contém transações realizadas entre **01/12/2010 e 09/12/2011** por uma empresa britânica de comércio eletrônico, especializada em presentes para todas as ocasiões.

**Fonte:** Dr. Daqing Chen, School of Engineering, London South Bank University, UK.

---

## 🎯 Objetivo
Construir um **pipeline completo de ETL** em Python para:  

1. Extrair o dataset via API do Kaggle  
2. Limpar e tratar os dados  
3. Armazenar em **.parquet**  
4. Carregar os dados no **SQL Server**  
5. Criar dashboards no **Power BI**  

O dashboard permite analisar:  
- Quantidade de produtos vendidos por país  
- Produtos mais vendidos  
- Valor total de vendas por país  

---
## 📂 Estrutura do Projeto
```
Online-Sales-UK---PR_ETL_01/
│
├── data/ # Arquivos de dados (ex: .parquet, .zip, .csv)
├── code/
│ ├── config.py # Conexão com o SQL Server
│ ├── import_dataset.py # Extração do dataset
│ ├── load.py # Load de dados no banco
│ ├── requirements.txt # Dependências do projeto
│ ├── exploration.py # Exploração e tratamento de dados 
├── database/ # Script utilizado no banco de dados
├── PB_PR_ETL_01/ # Arquivos do Power BI
└── README.md
```
---

## ⚙️ ETL – Etapas do Pipeline

### 1️⃣ Extração
- Dataset baixado via API do Kaggle.  
- Arquivo original em CSV importado para Python.

### 2️⃣ Transformação
- Limpeza de dados nulos e inconsistências.  
- Modularização em arquivos individuais: extração, transformação, load, conexão.  
- Arquivo final salvo em **.parquet** para performance otimizada.

### 3️⃣ Carga (Load)
- Dados carregados no **SQL Server**.  
- Conexão parametrizada via Python.

### 4️⃣ Análise e Dashboard (Power BI)
- Exclusão de registros de vendas canceladas.  
- Filtros de **data e país**.  
- Visualizações:  
  - Quantidade de produtos vendidos por país  
  - Produtos mais vendidos  
  - Valor total de vendas por país  

---

## 🛠 Tecnologias Utilizadas
- **Python:** pandas, pyodbc, sqlalchemy, parquet  
- **SQL Server:** Banco de dados relacional  
- **Power BI:** Dashboards e visualizações  

---


