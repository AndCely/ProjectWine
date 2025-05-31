import os
from pathlib import Path

# Obtiene la ruta absoluta del archivo actual
ruta_actual = Path(__file__).resolve()

# Sube dos niveles para llegar a la raíz del proyecto (ajusta según tu estructura)
raiz_proyecto = ruta_actual.parent.parent.parent

# Añade la raíz del proyecto al PYTHONPATH
os.environ["PYTHONPATH"] = str(raiz_proyecto)

# (Opcional) También puedes añadirlo a sys.path para el script actual:
import sys
if str(raiz_proyecto) not in sys.path:
    sys.path.append(str(raiz_proyecto))

import matplotlib.pyplot as plt
import seaborn as sns
from scripts.EstadisticosBasicos import ProcessData


class Graficador:
    def __init__(self):
        self.data = ProcessData().get_data()
        self.y_pred = ProcessData().obtener_y_pred()

    def graficar_distribucion(self):
       fig, axes = plt.subplots(4, 3, figsize=(15, 10))
       for i, column in enumerate(self.data.columns):
           ax = axes[i // 3, i % 3]  # Accede a los ejes correctos
           ax.set_title(column)
           sns.histplot(self.data[column], kde=True, ax=ax)
       plt.tight_layout(pad=3.0)
       return fig  # Devuelve la figura
    
    def graficar_boxplots(self):
        fig, axes = plt.subplots(4, 3, figsize=(15, 10))
        for i, col in enumerate(self.data.columns):
            ax = axes[i // 3, i % 3]  # Accede a los ejes correctos
            ax.set_title(col)
            sns.boxplot(x=self.data[col], ax=ax)
        plt.tight_layout(pad=3.0)
        return fig  # Devuelve la figura
    
    def grafica_correlacion(self):
        fig = plt.figure(figsize=(12, 8))
        sns.heatmap(self.data[self.data.columns].corr(), annot=True, cmap='coolwarm')
        plt.title('Matriz de Correlación')
        plt.tight_layout()
        return fig
    
    def graficar_regresionLineal(self):
        fig = plt.figure(figsize=(8, 6))
        plt.scatter(self.data['pH'], self.data['density'], alpha=0.6, label='Observaciones')
        plt.plot(self.data['pH'], self.y_pred, linewidth=2, label='Línea de regresión', color='red')
        plt.title('pH vs. Densidad (vino)')
        plt.xlabel('pH')
        plt.ylabel('Densidad')
        plt.legend()
        plt.tight_layout()
        return fig
    
    
if __name__ == "__main__":
    graficador = Graficador()
    
    while True:
        opcion = int(input(""" 
        Seleccione la opcion que quiere ver:
        - 1. Grafica distribucion
        - 2. Grafica boxplots
        - 3. Matriz de correlacion
        - 4. Regresion Lineal
        - 5. Salida
        """))
        if opcion == 1:
            fig = graficador.graficar_distribucion()
            plt.show()
            continue

        elif opcion == 2:
            fig = graficador.graficar_boxplots()
            plt.show()
            continue

        elif opcion == 3:
            fig = graficador.grafica_correlacion()
            plt.show()
        
        elif opcion == 4:
            fig = graficador.graficar_regresionLineal()
            plt.show()

        elif opcion == 5:
            break