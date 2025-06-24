# pip install requests types-requests

# TUtorial request API -> yt/Qd8JT0bnJGs
import requests 

# HTTP:// -> Porta 80
# HTTPs:// -> Porta 443

url = 'http://localhost:3333/'
response =  requests.get(url)
# Método (get) e  endereço (url)

print(response.status_code)
# Retorna o status code da pagina!
print(response.text)
# print(response.headers)
# print(response.content)
# print(response.json())