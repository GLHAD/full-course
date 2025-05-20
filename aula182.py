# secrets gera números aleatórios seguros
import secrets
import os

random = secrets.SystemRandom()

os.system('cls')

print(secrets.randbelow(100))
print(secrets.randbits(k=2))

print(secrets.choice([10,15,20]))

