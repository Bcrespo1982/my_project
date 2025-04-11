import streamlit as st
import pandas as pd
import plotly.express as px

# Lê o arquivo CSV e armazena no DataFrame
# car_data = pd.read_csv('vehicles.csv')
car_data = pd.read_csv(
    r'C:\Users\vivasetubalserver\Documents\MyProjects\my_project\notebooks\vehicles.csv')


hist_button = st.button('Criar histograma')  # criar um botão

if hist_button:  # se o botão for clicado
    # escrever uma mensagem
    st.write(
        'Criando um histograma para o conjunto de dados de anúncios de vendas de carros')

    # criar um histograma
    fig = px.histogram(car_data, x="odometer")

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

    import streamlit as st

# criar uma caixa de seleção
build_histogram = st.checkbox('Criar um histograma')

if build_histogram:  # se a caixa de seleção for selecionada
    st.write('Criando um histograma para a coluna odometer')

scatter_button = st.button('Criar gráfico de dispersão')

if scatter_button:
    st.write('Criando um gráfico de dispersão: preço vs. ano do carro')
    fig = px.scatter(car_data, x="model_year", y="price", title="Preço vs Ano do Carro",
                     labels={"model_year": "Ano do Modelo", "price": "Preço"})
    st.plotly_chart(fig, use_container_width=True)
