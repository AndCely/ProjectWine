import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# -*- coding: utf-8 -*-

# Cargar el conjunto de datos de vino tinto
""" Asegúrate de que el archivo 'winequality-red.csv' esté en la carpeta 'data'
Si no está, puedes descargarlo desde el repositorio de UCI Machine Learning Repository
https://archive.ics.uci.edu/ml/datasets/wine+quality
Nota: Este código asume que el archivo 'winequality-red.csv' está en la carpeta 'data'
Si el archivo no se encuentra, se lanzará una excepción FileNotFoundError"""

class ProcessData:
    def __init__(self):
        try:
            self.df = pd.read_csv('data/winequality-red.csv', sep=';', header=0)
        except FileNotFoundError as e:
            print("El archivo 'winequality-red.csv' no se encuentra en la carpeta 'data'.")
            raise e
        
    def get_data(self):
        return self.df
    
    def get_statistics(self):
        return self.df.describe()
    
    def get_statistics_by_column(self, column):
        return self.df[column].describe()
    


    # def estadisticos_basicos(self):
    #     """
    # Calcula estadísticos básicos de un DataFrame de pandas.
    
    # Args:
    #     df (pd.DataFrame): DataFrame con los datos.
    
    # Returns:
    #     pd.DataFrame: DataFrame con los estadísticos básicos.
    # """
    # estadisticos = pd.DataFrame({
    #     'Media': df.mean(),
    #     'Mediana': df.median(),
    #     'Desv Estándar': df.std(),
    #     'Coef de Desv': (df.std() / df.mean()) * 100,
    #     'Mínimo': df.min(),
    #     'Máximo': df.max()
    # })
    
    # return estadisticos

if __name__ == "__main__":
    process_data = ProcessData()
    df = process_data.get_data()
    print(df)
    print("-"*100)
    statistics = process_data.get_statistics()
    print(statistics)
    print("-"*100)
    statistics_by_column = process_data.get_statistics_by_column('quality')
    print(statistics_by_column)

    
    # Interfaz de usuario para mostrar los estadísticos básicos
    # print("Cálculo de estadísticos básicos del conjunto de datos de vino tinto:")
    # Calcular y mostrar los estadísticos básicos
    # estadisticos = estadisticos_basicos(df)
    # print(estadisticos)

# Graficar los estadísticos básicos
