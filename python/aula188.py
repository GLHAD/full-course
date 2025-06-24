# argparse.ArgumentParser para argumentos mais complexos

# Tutorial Oficial:
# https://docs.python.org/pt-br/3/howto/argparse.html

from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument(
    '-b', '--basic',
    help= 'Mostra "Olá mundo na tela"',
    # type= str,
    metavar= 'STRING',
    # default= 'Olá Mundo',
    required= False,
    action= 'append',                 # Adiciona valores em uma lista
    # nargs= '+'                      # Recebe mais de um valor
    ) 
# Required= True para forçar obrigatoriamente o envio do valor

args = parser.parse_args()

if args.basic is None:
    print('Você não passou o valor de basic')

else:
    print(args.basic)
    print('Do something')

