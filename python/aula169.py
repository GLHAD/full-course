# O módulo para os para interação com sistemas de arquivos.

# O módulo os é um módulo padrão do Python que fornece uma maneira de interagir com o 
# sistema operacional. Por exemplo, ele pode ser usado para manipular arquivos e 
# diretórios, obter informações sobre o sistema operacional e executar comandos 
# do sistema.

# A função os.listdir() é usada para listar os arquivos e diretórios em um diretório 
# específico.

# os.path trabalha com caminhos de arquivos e diretórios. Ele fornece funções para 
# manipular caminhos de arquivos, como criar caminhos, verificar se um caminho existe
# e obter informações sobre arquivos e diretórios.

# A função os.path.join() é usada para criar um caminho de arquivo ou diretório,
# unindo partes do caminho. Isso é útil para garantir que o caminho seja criado 
# corretamente, independentemente do sistema operacional em que o código está sendo 
# executado.

# A função os.path.exists() é usada para verificar se um caminho de arquivo ou
# diretório existe. Isso é útil para evitar erros ao tentar acessar arquivos ou
# diretórios que não existem. 

import os

caminho = os.path.join('aula168', 'aula168.txt')

