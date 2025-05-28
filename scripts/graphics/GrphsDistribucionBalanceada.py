import matplotlib.pyplot as plt
import seaborn as sns
from EstadisticosBasicos import ProcessData

class GrphsDistribucionBalanceada:
    def __init__(self):
        self.data = ProcessData().get_data()

    def graficar_distribucion_balanceada(self):
       fig, axes = plt.subplots(4, 3, figsize=(15, 10))
       for i, column in enumerate(self.data.columns):
           ax = axes[i // 3, i % 3]  # Accede a los ejes correctos
           ax.set_title(column)
           sns.histplot(self.data[column], kde=True, ax=ax)
       plt.tight_layout(pad=3.0)
       return fig  # Devuelve la figura
    
if __name__ == "__main__":
    GrphsDistribucionBalanceada().graficar_distribucion_balanceada()