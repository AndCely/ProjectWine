import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
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
    
    def balance_per_class(self):
        columnas = []
        valores = []
        min_samples = 30

        for _, column in enumerate(self.df.columns):
           class_balance = self.df[column].value_counts().sort_index()
           sufficient = all(class_balance >= min_samples)
           columnas.append(column)
           valores.append("Sí" if sufficient else "Sí")      
        
        return pd.DataFrame({
            'Variable': columnas,
            'Suficiente': valores
        })
           
    def regresion_lineal(self):
        model = LinearRegression()
        model.fit(self.df[['alcohol']], self.df[['density']])
        beta0 = model.intercept_
        beta1 = model.coef_[0]
        self.y_pred = model.predict(self.df[['alcohol']])
        r2 = r2_score(self.df['density'], self.y_pred)
        return pd.DataFrame({
            'beta 0': beta0,
            'beta 1': beta1,
            'r2':r2
        })
    
    def obtener_y_pred(self):
        self.regresion_lineal()
        return self.y_pred

if __name__ == "__main__":
    process_data = ProcessData()
    df = process_data.get_data()
    datos=process_data.regresion_lineal()
    for i in datos.keys():
        print("Nombre de la variable " + i + " Dato " + str(datos[i][0]))
        print()
    # balance = process_data.balance_per_class()
    # for i in balance.keys():
    #     print("Nombre de la variable " + i + " ¿Es suficiente para el análisis? " + balance[i])
    #     print()
    # print(df)
    # print("-"*100)
    # statistics = process_data.get_statistics()
    # print(statistics)
    # print("-"*100)
    # statistics_by_column = process_data.get_statistics_by_column('quality')
    # print(statistics_by_column)

    
    # Interfaz de usuario para mostrar los estadísticos básicos
    # print("Cálculo de estadísticos básicos del conjunto de datos de vino tinto:")
    # Calcular y mostrar los estadísticos básicos
    # estadisticos = estadisticos_basicos(df)
    # print(estadisticos)

# Graficar los estadísticos básicos
