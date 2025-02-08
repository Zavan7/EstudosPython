import json
from pprint import pprint
from typing import TypedDict

class Movie (TypedDict):
  title: str
  original_title: str
  is_movie: bool
  imdb_rating: float
  year: int
  characters: list [str]
  budget: None | float

string_json = '''
{
  "title": "O Senhor dos Anéis: A Sociedade do Anel",
  "original_title": "The Lord of the Rings: The Fellowship of the Ring",
  "is_movie": true,
  "imdb_rating": 8.8,
  "year": 2001,
  "characters": ["Frodo", "Sam", "Gandalf", "Legolas", "Boromir"],
  "budget": null
}
'''
filme: Movie = json.loads(string_json)

print (type(filme['imdb_rating']))
print (filme['title'])
print (filme ['year'])

json_str = (json.dumps(filme, ensure_ascii= False, indent= 2))
print (type(json_str))
print (json_str)