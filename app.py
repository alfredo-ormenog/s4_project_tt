import pandas as pd
import plotly_express as px
import streamlit as st

df_veh = pd.read_csv("C:/Users/Alfredo OG/Documents/Myprojects/s4_project_tt/s4_project_tt/dataset_veh/vehicles_us.csv")

st.header("¡Crea un Histograma!")
st.subheader("Este botón te permitirá realizar un Histograma con la información del dataset vehicules_us")

hist_button = st.button("Construir Histograma")

if hist_button:
    fig = px.histogram(df_veh, x="odometer")
    st.plotly_chart(fig, use_container_width=True)
