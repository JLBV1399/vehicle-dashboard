import streamlit as st
import pandas as pd
import plotly.express as px

# Título del dashboard
st.title("Análisis de Vehículos en EE.UU.")

# Cargar datos
@st.cache_data
def load_data():
    return pd.read_csv("vehicles_us.csv")  # <- Ruta corregida

df = load_data()

# Mostrar los datos
if st.checkbox("Mostrar datos crudos"):
    st.write(df.head())

# Histograma del odómetro
st.subheader("Distribución del Odómetro")
fig1 = px.histogram(df, x='odometer', nbins=100, title="Kilometraje de los vehículos")
st.plotly_chart(fig1)

# Gráfico de dispersión precio vs odómetro
st.subheader("Precio vs Kilometraje")
fig2 = px.scatter(df, x='odometer', y='price', title="Relación entre precio y kilometraje")
st.plotly_chart(fig2)
