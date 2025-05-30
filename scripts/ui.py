# Realizar las importaciones necesarias
import os
from pathlib import Path

# Obtiene la ruta absoluta del archivo actual
ruta_actual = Path(__file__).resolve()

# Sube dos niveles para llegar a la raíz del proyecto (ajusta según tu estructura)
raiz_proyecto = ruta_actual.parent.parent

# Añade la raíz del proyecto al PYTHONPATH
os.environ["PYTHONPATH"] = str(raiz_proyecto)

# (Opcional) También puedes añadirlo a sys.path para el script actual:
import sys
if str(raiz_proyecto) not in sys.path:
    sys.path.append(str(raiz_proyecto))

import streamlit as st
from EstadisticosBasicos import ProcessData
from settings import Settings
from scripts.graphics.Graficador import Graficador

class MainUI():
    """Clase principal para la interfaz de usuario de Streamlit."""
    def __init__(self):
        """Inicializa la interfaz de usuario de Streamlit."""
        # Inicializar la configuración de la aplicación
        self.settings = Settings()

        # Inicializar la interfaz de usuario para mostrar los estadísticos básicos
        self.display_ui = DisplayUI()
        
        # Configurar la página de Streamlit
        self._initialize_ui() 
        
    # Método para inicializar la interfaz de usuario
    def _initialize_ui(self):
        """Inicializa la interfaz de usuario de Streamlit."""
        # Configurar el título y la descripción de la aplicación
        st.set_page_config(
            page_title="Estadísticos Básicos del Conjunto de Datos de Vino Tinto",
            page_icon=":wine_glass:",
            layout="wide",
            initial_sidebar_state="expanded"
        )
        self._configure_sidebar()
        self._show_content()

    def _configure_sidebar(self):
        st.sidebar.title("Menú de Navegación")
        self.opcion = st.sidebar.radio(
            "Selecciona una opción:",
            self.settings.options
        )

    def _show_content(self):
        """Muestra el contenido de la aplicación según la opción seleccionada."""
        # Mostrar el contenido basado en la opción seleccionada
        st.sidebar.markdown("---")
        if self.opcion == "Inicio":
            self.display_ui.display_home()
        elif self.opcion == "Estadisticas Básicas":
            self.display_ui.display_statistics()
        elif self.opcion == "Gráficos":
            self.display_ui.display_graphs()
        elif self.opcion == "Configuración":
            self.display_ui.display_configuration()

class DisplayUI:
    """Clase para mostrar la interfaz de usuario de Streamlit."""
    def __init__(self):
        """Inicializa la interfaz de usuario de Streamlit."""
        # Inicializa la configuración de la aplicación
        self.settings = Settings()

        # Inicializa el conjunto de datos de vino tinto
        self.process_data = ProcessData()

        # Inicializa los graficos
        self.graficador = Graficador()

    def display_statistics(self):
        st.title("Estadisticas Básicas")
        st.subheader("DataSet")
        st.dataframe(self.process_data.get_data())
        st.subheader("Estadistica Basica del Conjunto de Datos")
        st.markdown("""
        Esta sección muestra los estadísticos básicos calculados 
        para el conjunto de datos de vino tinto.
        """)
        st.dataframe(self.process_data.get_statistics())

        st.subheader("Tamaño muestral")
        st.dataframe(self.process_data.balance_per_class())

        st.subheader("Regresion lineal: Alcohol/Densidad")
        st.dataframe(self.process_data.regresion_lineal())

    def display_graphs(self):
        """Muestra los gráficos relacionados con el conjunto de datos de vino tinto."""
        st.title("Gráficos de Estadísticos Básicos del Conjunto de Datos de Vino Tinto")
        st.markdown("""        Esta sección muestra gráficos relacionados con los estadísticos básicos del conjunto de datos de vino tinto.
        Los gráficos incluyen la media de cada variable y otros estadísticos relevantes.
        """)

        # Mostrar los gráficos de la distribución
        st.subheader("Gráficos de Distribución")
        fig = self.graficador.graficar_distribucion()
        st.pyplot(fig)

        # Mostrar los gráficos de boxplots
        st.subheader("Gráficos de Boxplots")
        fig = self.graficador.graficar_boxplots()
        st.pyplot(fig)

        # Mostrar la matriz de correlacion
        st.subheader("Matriz de correlacion")
        fig = self.graficador.grafica_correlacion()
        st.pyplot(fig)

        # Mostrar la regresion lineal alcohol/densidad
        st.subheader("Matriz de correlacion")
        fig = self.graficador.graficar_regresionLineal()
        st.pyplot(fig)
        

    def display_home(self):
        """Ejecuta la aplicación Streamlit."""
         # Mostrar un mensaje de bienvenida
        st.title("Estadísticos Básicos del Conjunto de Datos de Vino Tinto")
        st.markdown("""
        Esta aplicación interactiva te sumerge en el mundo de los estadísticos básicos del conjunto de datos de vino tinto. 
        Su propósito principal es facilitar la exploración y comprensión de las características numéricas de este dataset,
        permitiéndote desglosar y visualizar la información de una manera sencilla y efectiva.
        """)
        st.subheader("¿Qué puedes explorar?")
        st.markdown("""
            - Estadísticos descriptivos: Obtén un resumen rápido de las variables clave del vino, como la acidez, el pH, el contenido de alcohol, etc. Esto incluirá métricas como la media, mediana, moda, desviación estándar, varianza, cuartiles y rango, que te darán una primera impresión de la distribución de los datos.
            - Visualizaciones gráficas: La aplicación generará gráficos relevantes que te ayudarán a entender mejor los datos. Esto podría incluir:
                - Histogramas para ver la distribución de cada variable.
                - Diagramas de caja y bigotes (box plots) para identificar valores atípicos y la dispersión de los datos.
                - Diagramas de dispersión (scatter plots) para explorar la relación entre dos variables diferentes (por ejemplo, cómo el pH se relaciona con la acidez fija).
                - Gráficos de barras para comparar categorías si el conjunto de datos incluye variables cualitativas.
            - Análisis de correlación: Es posible que la aplicación también ofrezca una matriz o mapa de calor de correlación, que te permitirá ver cómo se relacionan entre sí las diferentes propiedades químicas del vino. Esto es útil para identificar qué características influyen en otras.
            - Filtrado y segmentación: Algunas aplicaciones avanzadas podrían permitirte filtrar el conjunto de datos según ciertos criterios (por ejemplo, vinos con un pH específico o un contenido de alcohol superior a cierto valor) para analizar subconjuntos de datos.
        """)
        st.subheader("Beneficios de la aplicación")
        st.markdown("""
            - Mejora la comprensión de los datos: La aplicación te permite ver los datos de manera visual, lo que facilita entender las relaciones y tendencias.
            - Ahorra tiempo: En lugar de calcular estadísticos manualmente, puedes usar la aplicación para obtener resultados rápidos.
            - Fomenta la exploración: La aplicación te permite probar diferentes visualizaciones y estadísticos para encontrar patrones y tendencias.
            - Mejora la toma de decisiones: Al entender mejor los datos, puedes tomar decisiones más informadas sobre el vino.
        """)

        st.write("**Selecciona una opción del menú lateral para comenzar.**")

    def display_configuration(self):
        """Muestra la configuración de la aplicación."""

        st.title("Configuración de la Aplicación")
        st.markdown("""
        Esta sección te permite ajustar la configuración de la aplicación.
        Puedes cambiar el tema, idioma y otras opciones de configuración.
        """)

        # Mostrar la configuración actual
        st.subheader("Configuración")
        st.write("Aquí puedes ajustar la configuración de la aplicación.")
        # Aquí podrías agregar opciones para cambiar el tema, idioma, etc.
        st.write("Configuración actual:", self.settings.settings)

if __name__ == "__main__":
    # Ejecutar la aplicación
    ui = MainUI()