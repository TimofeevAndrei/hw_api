import json
import requests
from pprint import pprint

url = requests.get('https://akabab.github.io/superhero-api/api/all.json')
res = json.loads(url.text)
superheroes = {}
for x in res:
    name = x.get('name')
    pwrst = x.get('powerstats')
    superheroes.update({name: pwrst.get('intelligence')})
# pprint(superheroes)

max_value = max(superheroes.values())
top_intelligence = {k: v for k, v in superheroes.items() if v == max_value}
pprint(top_intelligence)
