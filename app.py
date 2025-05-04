import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv('vehicles_us.csv') # leer los datos
#hist_button = st.button('Construir histograma') # crear un botón

st.header("Dashboard de Vehículos")
        
#if hist_button: # al hacer clic en el botón
            # escribir un mensaje
    #st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
    #fig = px.histogram(car_data, x="odometer")
        
            # mostrar un gráfico Plotly interactivo
    #st.plotly_chart(fig, use_container_width=True)

# Casilla para el histograma
show_histogram = st.checkbox("Mostrar Histograma de Precios")
if show_histogram:
    st.write("Histograma de la distribución de precios")
    fig = px.histogram(car_data, x="price", title="Distribución de Precios")
    st.plotly_chart(fig)

# Casilla para el gráfico de dispersión
show_scatter = st.checkbox("Mostrar Gráfico de Dispersión")
if show_scatter:
    st.write("Gráfico de dispersión: Precio vs Año")
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig)