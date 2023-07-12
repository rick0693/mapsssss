import time
import pandas as pd
from urllib.parse import quote
from selenium import webdriver

# Carregar a planilha
planilha = pd.read_excel('cidades.xlsx')

# Obter as colunas "cidade" e "estado" como listas
cidades = planilha['cidade'].tolist()
estados = planilha['estado'].tolist()

# Combinar os valores das colunas cidade e estado
enderecos = []

for cidade, estado in zip(cidades, estados):
    endereco = f"{cidade}, {estado}"
    enderecos.append(quote(endereco))

# URL da rota
url_rota = f"https://www.google.com/maps/dir/{'/'.join(enderecos)}"

# Imprimir o link da rota
print(f"Link de rota: {url_rota}")

# Configurar o WebDriver do Selenium
driver = webdriver.Chrome()

# Acessar a URL da rota
driver.get(url_rota)

# Pausa de 10 segundos para visualizar o mapa
time.sleep(300)

# Fechar o navegador
driver.quit()
