import json
import requests
from pprint import pprint
#Самый умный из троих: Hulk, Captain America, Thanos.

url = requests.get('https://akabab.github.io/superhero-api/api/all.json')
res = json.loads(url.text)
superheroes = {}
for x in res:
    name = x.get('name')
    pwrst = x.get('powerstats')
    superheroes.update({name: pwrst.get('intelligence')})

top_heroes = []
heroes = ['Hulk', 'Thanos', ' Captain America']
for item in superheroes.items():
    name, intell = item
    for i in heroes:
        if name == i:
            top_heroes.append(list(item))

top_heroes.sort(reverse=True)
print(top_heroes[0][0])



# Задание №2

