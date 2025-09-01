import pandas as pd

def Exploration ():
    # Carregar os dados
    df = pd.read_csv("./data/data.csv", encoding="ISO-8859-1")  # esse dataset costuma dar erro de encoding sem isso

    # Ver primeiras linhas
    print(df.head())

    # Total de linhas por coluna (contando valores não nulos)
    print(df.count())
    
    # Remove linhas onde CustomerID ou Description sejam nulos
    df_clean = df.dropna(subset=["CustomerID", "Description"])

    print("Antes:", len(df))
    print("Depois:", len(df_clean))
    
    # Converter InvoiceDate para datetime
    df_clean["InvoiceDate"] = pd.to_datetime(df_clean["InvoiceDate"], errors="coerce")

    # Conferir se teve conversão inválida
    print("Datas inválidas:", df_clean["InvoiceDate"].isna().sum())

    print(df_clean.head())

    # Criar coluna de valor total por venda
    df_clean["TotalPrice"] = df_clean["Quantity"] * df_clean["UnitPrice"]
    df_clean['CustomerID'] = df_clean['CustomerID'].astype(int)
    

    print(df_clean.head())

    # Colocar dados tratados no arquivo .parket
    df_clean.to_parquet("./data/clean_data.parquet", engine="pyarrow", index=False)

    
 

