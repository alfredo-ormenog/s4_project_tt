# Importar las librerías necesarias:
import pandas as pd
import plotly_express as px
import streamlit as st
# PRIMERA PARTE:
# CREAR HISTOGRAMA Y GRÁFICO DE DISPERSIÓN:

# Leer el dataset:
df_veh = pd.read_csv("./dataset_veh/vehicles_us.csv")

# Crear el título de la página y un subtítulo:
st.header("¡Escoge el gráfico de tu preferencia!")
st.subheader("Marca la casilla el gráfico que desees analizar")

chart_names = ["Histograma", "Gráfico de Dispersión"]
opt_chart_names = st.radio("Selecciona:", chart_names)

st.write("El gráfico escogido ha sido: ", opt_chart_names)

# Crear los gráficos:
if opt_chart_names == "Histograma":
    st.subheader("Histograma")
    st.write("""**Definición:**\n Gráfico de la representación de distribuciones de frecuencias, 
             en el que se emplean rectángulos dentro de unas coordenadas.
             Ayudan a ver el centro, la extensión y la forma de un conjunto de datos.
             También se pueden usar como herramienta visual para comprobar la normalidad.             
             """)
    app = st.checkbox("Mostrar gráfica")
    if app:
        fig = px.histogram(df_veh, x="odometer")
        st.plotly_chart(fig, use_container_width=True)
else:
    st.subheader("Gráfico de Dispersión")
    st.write("""Es una herramienta no espacial que sirve para visualizar la relación entre dos variables continuas. 
             Se utilzan para mostrar relaciones,Para la correlación, muestran la fuerza de la relación lineal entre
              dos variables. Para la regresión, los gráficos de dispersión suelen incorporar una línea de ajuste. """)
    app_2 = st.checkbox("Mostrar gráfica")
    if app_2:
        fig_2 = px.scatter(df_veh, x="odometer")
        st.plotly_chart(fig_2, use_container_width=True)


# hist_button = st.button("Construir Histograma")
# scat_button = st.button("Construir Gráfico de Dispersión")

# Creando el botón para creación de HISTOGRAMAS:
# if hist_button:
    # fig = px.histogram(df_veh, x="odometer")
    # st.plotly_chart(fig, use_container_width=True)


# Creando el botón para creación de GRÁFICO DE DISPERSIÓN:
# if scat_button:
 #   fig_2 = px.scatter(df_veh, x="odometer")
  #  st.plotly_chart(fig_2, use_container_width=True)


# SEGUNDA PARTE:
# Tabla que muestre los vehículos por casa manufacturera:
