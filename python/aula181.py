# random tem geradores de números pseudoaleatórios

# Obs: números pseudoaleatórios significa que os números parecem ser aleatórios,
# mas na verdade não são. Portanto esse módulo não deve ser usado para segurança 
# ou criptográfias. 

# O motivo disso é que quando temos uma mesma entrada e mesmo algorítmo, a saida 
# pode ser previsível. 
import random
import os

os.system('cls')
# Funções:
#   seed: 
#       Inicializa o gerador de random.
# random.seed()

#   random.randrange(start, stop, step):
#       Gera um número inteiro aletório dentro de um intervalo de espaço.
r_range = random.randrange(0, 10, 2)
print(f'Random range: {r_range}')

#   random.randint(start, end):
#       Gera um número inteiro aleatório dentro do intervalo "sem passo".
r_int = random.randint(0, 10)
print(f'Random int: {r_int}')

#   random.uniform(start, stop):
#       Gera um número flutuante aletório dentro de um intervalo de espaço "sem".
r_uniform = random.uniform(0, 10)
print(f'Random Uniform: {r_uniform:.2f}')

#   random.shuffle(SequenciaMutavel):
#       Embaralha uma lista original.
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f'Original list: {list}')
r_shuffle = random.shuffle(list)
print(f'Random shuffle: {list}')

#   random.sample(Iteravel, k=N):
#       Escolhe elementos do iterável e retorna outro iterável (não repete).
new_list = random.sample(list, k= 5)
print(f'Original list: {list}')
print(f'Sample List: {new_list}')

#   random.choice(Iteravel):
#       Escolhe elementos do iterável.
print(f'Choice: {random.choice(list)}')

#   random.choices(Iteravel, k=N):
#       Escolhe elementos do iterável e retorna outro iterável (repete).
choice_list = random.choices(list, k= 5)
print(f'Choices: {choice_list}')

