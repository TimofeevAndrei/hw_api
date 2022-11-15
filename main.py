import json
import requests
from pprint import pprint
#Самый умный из троих: Hulk, Captain America, Thanos.
#
# url = requests.get('https://akabab.github.io/superhero-api/api/all.json')
# res = json.loads(url.text)
# superheroes = {}
# for x in res:
#     name = x.get('name')
#     pwrst = x.get('powerstats')
#     superheroes.update({name: pwrst.get('intelligence')})
#
# top_heroes = []
# heroes = ['Hulk', 'Thanos', ' Captain America']
# for item in superheroes.items():
#     name, intell = item
#     if name in heroes:
#             top_heroes.append(list(item))
#
# top_heroes.sort(reverse=True)
# print(top_heroes[0][0])



# Задание №2
token = 'token.txt'
class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'}

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        print('2')
        # Тут ваша логика
        # Функция может ничего не возвращать

    def get_link(self, path):
        uri = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        params = {'path': path, 'overwrite': True}
        response = requests.get(uri, headers=self.get_headers(), params=params)
        return response

if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = 'test.txt'
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
    print('1')
