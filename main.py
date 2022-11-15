import json
import requests
from settings import TOKEN
from pprint import pprint

# Самый умный из троих: Hulk, Captain America, Thanos.

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
    if name in heroes:
            top_heroes.append(list(item))

top_heroes.sort(reverse=True)
print(top_heroes[0][0])



# Задание №2

class YaUploader:

    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'}

    def upload(self, local_path, ya_path):
        ya_path = local_path
        """Метод загружает файлы по списку file_list на яндекс диск"""
        upload_url = self.get_link(ya_path)
        response = requests.put(upload_url, data=open(local_path, 'rb'), headers=self.get_headers())
        if response.status_code == 201:
            print(f'Загрузка файла',
            local_path, 'прошла успешно!')

    def get_link(self, path):
        uri = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        params = {'path': path, 'overwrite': True}
        response = requests.get(uri, headers=self.get_headers(), params=params)
        # print(response.json())
        return response.json()['href']

if __name__ == '__main__':
    file_list = ['test.txt', 'test2.txt']
    ya = YaUploader(TOKEN)
    for x in file_list:
        ya.upload(x, 'name')

