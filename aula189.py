# O módulo requests para requisições HTTP no Python

# HTTP (HyperText Transfer Protocol) é um protocolo usado para enviar e receber
# dados na internet. Ele funciona no modo cliente/servidor, onde o cliente faz uma
# requisição ao servidor.

# A mensagem de requisição do cliente deve incluir dados como:
# O método HTTP
#   - Leitura (safe) - GET. HEAD. OPTIONS (métodos suportados)
#   - escrita - POST, PUT(substitui), PATCH (atualiza), DELETE

# - O endereço do recurso a ser acessado (/Users/)
# - Os cabeçalhos HTTP (Content-Type, Authorization)
# - O Corpo da mensagem (Caso necessário, de acordo com o médodo)

# A resposta do servidor deve incluir dados como:
# - Código de Status HTTP (200 sucess, 404 Not Found, 301 Moved Permanently)
# - Os cabeçalhos HTTP (Content-Type, Accept)
# - O corpo da mensagem (Pode estar vazio em alguns casos)


# py -m http.server -d aula190_site/ 3333