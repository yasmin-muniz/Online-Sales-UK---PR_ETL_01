import os
import zipfile

# Criar pasta para guardar os dados
os.makedirs("data", exist_ok=True)

# Baixar o dataset (API Kaggle precisa estar configurada)
os.system("kaggle datasets download -d carrie1/ecommerce-data -p ./data")

# Descompactar  
with zipfile.ZipFile("./data/ecommerce-data.zip", 'r') as zip_ref:
    zip_ref.extractall("./data")

print("Download concluído e descompactado!")



# rodar no cmd
# python Import_DataSet.py
# colocar .json do kaggle nesse diretorio caso o download não funcione
# C:\Users\SEU_USUARIO\.kaggle\kaggle.json


