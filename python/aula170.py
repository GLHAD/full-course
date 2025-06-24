# os.listdir para navegar em caminhos.

# Exemplo
# caminho = r'D:\PROJETOS\CURSO\aula170.py'

import os
from itertools import count

caminho = os.path.join('/PROJETOS', 'CURSO', 'exemplo')
print(caminho)

counter = count()

for item in os.listdir(caminho):
    print(item)

# os.walk é uma função que permite percorrer uma estrutura de diretórios de maneira 
# recursiva. Ela gera uma sequencia de tuplas, onde cada tupla possui três elementos:
#   O diretorio atual (root),
#   Uma lista de subdiretórios (dirs),
#   Uma lista de arquivos do diretório atual (files)

for root, dirs, files in os.walk(caminho):
    the_counter = next(counter)
    print(root)