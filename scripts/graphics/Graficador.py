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
        fig = plt.figure(figsize=(6, 4))
        plt.scatter(self.data['alcohol'], self.data['density'], alpha=0.6, label='Observaciones')
        plt.plot(self.data['alcohol'], self.y_pred, linewidth=2, label='Línea de regresión')
        plt.title('Alcohol vs. Densidad (vino)')
        plt.xlabel('Alcohol')
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