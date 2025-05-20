# csv.writer e csv.DictWriter

# csv.writer escreve o CSV em formato de lista
# csv.DictWriter escreve o CSV em formato de dicionário

import os
import csv
from pathlib import Path

os.system('cls')
FILE_CSV = Path(__file__).parent / 'aula180.csv'

client_list = [
    {'Name': 'Adryel Otto', 'Address': 'Av. Brasilia, 4380'},
    {'Name': 'Aline Persona', 'Address': 'Rua Alfredo Jaime Fellipe, 130'},
    {'Name': 'Matheus Gimenes', 'Address': 'Roberto Lambach, 92'},
    {'Name': 'Vinicius Knauber', 'Address': 'Humberto Geronasso, 72'},
]

#   ---- ESCREVER EM FORMATO DE LISTAS ----
# with open(FILE_CSV, 'w', newline='', encoding='utf-8') as file:
#     name_column = client_list[0].keys()
#     writer = csv.writer(file)
#     writer.writerow(name_column)
#     for client in client_list:
#         writer.writerow(client.values())


#   ---- ESCREVER EM FORMATO DE DICIONÁRIO ----
with open(FILE_CSV, 'w', newline='', encoding='utf-8') as file:
    name_column = client_list[0].keys()
    writer = csv.DictWriter(
        file,
        fieldnames=name_column
    )
    writer.writeheader()

    for client in client_list:
        writer.writerow(client)
   
