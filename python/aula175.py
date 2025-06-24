# O que é JSON?

# JSON - JavaScript Object Notation é uma estrutura de dados permite a serialização
# de objetos com texto simples para facilitar a transmissão de dados atráves da rede
# API's web e outros meios de comunicação. 

# O JSON é baseado em dois tipos de estruturas:
    # Numeros: inteiros, reais, booleanos e nulos
    # Strings: texto, listas e dicionários
    # Booleanos: True e False
    # Arrays: listas ordenadas de valores
    # Objetos: São conjuntos de pares chave-valor
    # Null: Representa um valor nulo ou vazio

# Ao converter de Python para JSON, o Python converte os tipos de dados nativos do
# Python para tipos equivalentes em JSON. Por exemplo:
    # - Dicionários Python se tornam objetos JSON
    # - Listas e tuplas Python se tornam arrays JSON
    # - Strings Python se tornam strings JSON
    # - Números Python se tornam números JSON
    # - Valores booleanos Python se tornam valores booleanos JSON (true/false)
    # - None em Python se torna null em JSON

# json.dumps() - Converte um objeto Python em uma string JSON
# json.loads() - Converte uma string JSON em um objeto Python

import json
from pprint import pprint       # Para imprimir de forma mais legível
from typing import TypedDict    # Para criar um dicionário tipado

class Movie(TypedDict):
    title: str
    original_title: str
    is_movie: bool
    imdb_rating: float
    release_year: int
    characters: list[str]
    budget: float | None

string_json = '''{
    "title": "O Senhor dos Anéis: A Sociedade do Anel",
    "original_title": "The Lord of the Rings: The Fellowship of the Ring",
    "is_movie": true,
    "imdb_rating": 8.8,
    "release_year": 2001,
    "characters": ["Frodo", "Sam", "Gandalf", "Legolas", "Boromir"],
    "budget": null
}
'''
print(string_json)

movie: Movie = json.loads(string_json)
# pprint(movie, width= 40)
# print(movie['title'])
# print(movie['characters'])
# print(movie['characters'][0])

json_string = json.dumps(movie, ensure_ascii=False, indent=2)
