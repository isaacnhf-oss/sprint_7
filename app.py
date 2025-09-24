import pandas as pd
import streamlit as st
import plotly.graph_objects as go

car_data = pd.read_csv('vehicles_us.csv')

st.header("Muestra de gráficas")

# Crear un botón en la aplicación Streamlit
hist_button = st.button('Construir histograma')

# Lógica a ejecutar cuando se hace clic en el botón
if hist_button:
    # Escribir un mensaje en la aplicación
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # Crear un histograma utilizando plotly.graph_objects
    # Se crea una figura vacía y luego se añade un rastro de histograma
    fig = go.Figure(
        data=[
            go.Histogram(
                x=car_data['odometer']
                )
            ]
        )

    # Opcional: Puedes añadir un título al gráfico si lo deseas
    fig.update_layout(
        title_text='Distribución del Odómetro'
        )

    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    # 'use_container_width=True' ajusta el ancho del gráfico al contenedor
    st.plotly_chart(
        fig, 
        use_container_width=True
        )

scatter_button = st.checkbox('Construir gráfico de dispersión')

if scatter_button:

    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de ventas de coches')
    

    fig2 = go.Figure(
        data=[
            go.Scatter(
                x=car_data['odometer'], 
                y=car_data['price'], 
                mode='markers',
                marker=dict(color="green")
                )
            ]
        )

    fig2.update_layout(title_text='Relación entre Odómetro y Precio')
    st.plotly_chart(fig2, use_container_width=True)

st.write("Datos de la tabla vehiculos")
st.dataframe(car_data)

# Prepara una tabla que muestras el año del modelo y los dias que ha estado listado
car_year_days = car_data.dropna(inplace=True)
car_year_days = car_data[['model_year', 'days_listed']]

# Despliega una gráfica de dispersión que muestra la información de car_year_days
fig3 = go.Figure(
    data=[
        go.Scatter(
            y=car_year_days['days_listed'], 
            x=car_year_days['model_year'], 
            mode='markers', 
            marker=dict(color="orange")
            )
        ]
    )

fig3.update_layout(title_text='Relación entre dias en lsitado y año del modelo')
st.plotly_chart(fig3, use_container_width=True)

# Botón para crear el gráfico de barras
st.header("Comparación de los modelos")
model_button = st.button('Construir grafico de barras')

# Lógica a ejecutar cuando se hace clic en el botón
if model_button:
    # Escribir un mensaje en la aplicación
    st.write('Creación de un gráfico de barras que muestra la cantidad de carros para un modelo')
    tabla = car_data['model'].value_counts().reset_index()

    # Crea un gráfico de barras para contar los diferentes moldelos
    fig4 = go.Figure(
        data=[
            go.Bar(
                x=tabla['model'], 
                y=tabla['count'],
                marker=dict(color="lime")
                )
            ]
        )
    
    fig4.update_layout(title_text='Cantidad de autos por modelo')
    st.plotly_chart(fig4, use_container_width=True)