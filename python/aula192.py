# - Web Scraping com Python usando requests e BS4 BeautifulSoup 
# - Web Scraping é o ato de 'raspar a web' buscando informações de forma 
# automatizada, com determinada linguagem de programação, para o uso posterior.

# O módulo requests consegue carregar dados da Internet para dentro do seu code.
# Já o bs4.BeautifulSoup é responsavel por interpretar os dados HTML em formato 
# de objetos Python para facilitar a vida do dev.

# pip install requests types-requests bs4

import requests
from bs4 import BeautifulSoup

url = 'http://127.0.0.1:3333'
response = requests.get(url)

print(response)

raw_html = response.text

parsed_html = BeautifulSoup(raw_html, 'html.parser')