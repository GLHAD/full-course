# csv.reader e csv.DictReader

# csv.reader lê o CSV em formato de lista
# csv.DictReader lê o CSV em formato de dicionário

import os
import csv
from pathlib import Path

FILE_CSV = Path(__file__).parent / 'aula179.csv'

os.system('cls')
print('----Ler em formato de listas----') 
with open(FILE_CSV, 'r', encoding='utf-8') as file: 
    reader = csv.reader(file)
    # next(reader)      # Posso usar next para pular a primeira linha
    for i in reader:
        print(i)
print()

print('----Ler em formato de Dicionário----')
with open(FILE_CSV, 'r', encoding='utf-8') as file: 
    reader = csv.DictReader(file)
    # next(reader)      # Posso usar next para pular a primeira linha
    for i in reader:
        print(i['Nome'], i['Idade'], i['Endereço'])
print()