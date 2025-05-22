# sys.argv -  Executando arquivos com argumentos no sistema
# Fonte = Fira Code

import sys

argumento = sys.argv
qtd_argumentos =  len(argumento) 

# print(qtd_argumentos)

if qtd_argumentos <= 1:
    print('Você não passou argumentos')

else:
    try:
        print(f'você passou os argumentos {argumento[1:]}')
        print(f'Faça algo com o {argumento[1]}')
    except IndexError:
        print(f'Faltam argumentos listados')