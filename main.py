import requests 

# Задание 1

def get_hero_with_max_int():
    url='https://akabab.github.io/superhero-api/api/all.json'
    response = requests.get(url).json()
    our_heroes = ['Thanos', 'Captain America', 'Hulk']
    our_heroes_int = {}
    for hero in our_heroes:
        for content in response: 
            if content['name'] == hero:
                our_heroes_int[hero] = int(content['powerstats']['intelligence'])
    max_int = 0
    for hero in our_heroes_int.keys():
        if max_int < our_heroes_int[hero]:
            max_int, hero_with_max_int = our_heroes_int[hero], hero
    return hero_with_max_int

# print('Герой с самым высоким показателем интеллекта:', get_hero_with_max_int())

# Задание 2

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, path_to_file: str):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {token}'}
        params = {'path' : path_to_file, 'overwrite': 'true'}
        response_with_upload_link = requests.get(url, headers=headers, params=params).json()
        upload_link = response_with_upload_link.get('href')
        response = requests.put(upload_link, data=open(path_to_file, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            return 'Success'
        else:
            error = f'Код ошибки: {response.status_code}'
            return error

if __name__ == '__main__':
    path_to_file = '1.jpeg' # Файл находится в одной папке с main.py
    token = '' # Вставить токен 
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)

# print(result)