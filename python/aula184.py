# Variáveis de ambiente com Python

# Para variáveis de ambiente
# Windows PowerShell: $env: VARIAVEL="VALOR" | dir env:
# Linux e Mac: export NOME_VARIAVEL ="VALOR" | echo $VARIAVEL

# Para obter o valor das variáveis de ambiente:
#   os.getenv ou os.environ['VARIAVEL']

# Para configurar variáveis de ambiente:
#   os.environ['VARIAVEL'] = 'valor'

# Ou usando python-dotenv e o arquivo .env
#   pip install python-dotenv
#   from dotenv import load_dotenv
#   load_dotenv()

# OBS: ---SEMPRE--- lembre-se de criar um .env-example

import os
from dotenv import load_dotenv

load_dotenv()

# print(os.environ)
print(os.getenv('BD_PASS'))