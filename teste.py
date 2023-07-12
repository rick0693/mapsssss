import streamlit as st
import pandas as pd
from urllib.parse import quote
from selenium import webdriver

# Carregar a planilha usando o Streamlit
uploaded_file = st.sidebar.file_uploader("Selecione a planilha", type=["xlsx"])
if uploaded_file is not None:
    planilha = pd.read_excel(uploaded_file)

    # Obter as cidades únicas da planilha
    cidades_unicas = planilha['cidade'].unique()

    # Selecionar as cidades para gerar o link da rota
    cidades_selecionadas = st.sidebar.multiselect("Selecione as cidades", cidades_unicas)

    # Filtrar o DataFrame com base nas cidades selecionadas
    planilha_filtrada = planilha[planilha['cidade'].isin(cidades_selecionadas)]

    # Verificar duplicidade entre estados e cidades
    combinacoes = set()
    enderecos = []
    for _, row in planilha_filtrada.iterrows():
        endereco = f"{row['cidade']}, {row['estado']}"
        combinacao = (row['cidade'], row['estado'])
        if combinacao not in combinacoes and endereco not in enderecos:
            enderecos.append(quote(endereco))
            combinacoes.add(combinacao)

    # Botão para gerar o link da rota
    if st.sidebar.button("Gerar link"):
        # URL da rota
        url_rota = f"https://www.google.com/maps/dir/{'/'.join(enderecos)}"

        # Exibir o link da rota
        st.sidebar.write("## Link de Rota")
        st.sidebar.write(url_rota)

        # Configurar o WebDriver do Selenium
        driver = webdriver.Chrome()

        # Acessar a URL da rota
        driver.get(url_rota)

    # Exibir os DataFrames lado a lado
    st.write("## DataFrames")
    col1, col2 = st.columns(2)
    col1.write("### DataFrame Original")
    col1.write(planilha)
    col2.write("### DataFrame Filtrado")
    col2.write(planilha_filtrada)
