# json.dump e json.load com arquivos

import json
import os

FILE_NAME = 'aula177.json'
ABS_PATH =  os.path.abspath(
    os.path.join(os.path.dirname(__file__), FILE_NAME)
)
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
# print(json.loads(string_json))

movie = {
    "title": "O Senhor dos Anéis: A Sociedade do Anel",
    "original_title": "The Lord of the Rings: The Fellowship of the Ring",
    "is_movie": True,
    "imdb_rating": 8.8,
    "release_year": 2001,
    "characters": ["Frodo", "Sam", "Gandalf", "Legolas", "Boromir"],
    "budget": None
}

print(movie)

with open(ABS_PATH, 'w') as file:
    json.dump(movie, file, ensure_ascii=False, indent=2) 

with open(ABS_PATH, 'r') as file:
    json_movie = json.load(file)
    print(json_movie)