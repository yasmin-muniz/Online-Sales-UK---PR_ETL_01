# pipeline.py

from Import_DataSet import Import_DataSet
from Exploration import Exploration
from Load import Load 

def main():
    print("🔹 Iniciando pipeline ETL...")
  
    # Extração
    Import_DataSet()
    print("Dataset pronto para transformação!")

    # Transformação
    Exploration()
    print("Transformação concluída")

    # Load
    Load()
    print("Load Finalizado")

    print("Pipeline ETL finalizado com sucesso!")

if __name__ == "__main__":
    main()
