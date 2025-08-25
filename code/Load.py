import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.types import Integer, String, Float, DateTime
from Config import server, database, username, password

# --- Passo 1: Carregar os dados tratados ---
df_clean = pd.read_parquet("./data/clean_data.parquet")

# --- Passo 2: Conectar ao banco ---
conn_str = f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=no"
engine = create_engine(conn_str)

# --- Passo 3: Mapear tipos de dados (opcional, mas evita erros) ---
dtype_mapping = {
    'InvoiceNo': String(20),
    'StockCode': String(20),
    'Description': String(255),
    'Quantity': Integer(),
    'InvoiceDate': DateTime(),
    'UnitPrice': Float(),
    'CustomerID': Integer(),
    'Country': String(100)
}

# --- Passo 4: Inserir os dados ---
df_clean.to_sql('Orders', con=engine, if_exists='append', index=False, dtype=dtype_mapping)

print("Carga concluída!")
