import requests
import json
#from pprint import pprint
import my_logger

logger = my_logger.get_logger(__name__)

class VkUser:
    url = 'https://api.vk.com/method/photos.get'

    def __init__(self, id, album = 'profile'):
        with open('token.txt') as f:
            self.token = f.read().strip()
        self.album_id = album
        self.id = id
        self.params = {
            'owner_id': self.id,
            'access_token': self.token,
            'album_id': self.album_id, #'wall', #'profile',
            'rev': '0',
            'extended': '1',
            'v': '5.130'
        }
    # Получаем информацию о юзере (строка "Имя_Фамилия"):
    def user_info(self):
        url = 'https://api.vk.com/method/users.get'
        params = {
            'user_id': self.id,
            'access_token': self.token,
            'v': '5.130'
        }
        info = requests.get(url, params=params)
        # Проверка валидности ID:
        if "error" in info.json().keys():
            print('ошибка: ', info.json()['error']['error_msg'])
            logger.error(info.json()['error']['error_msg'])
            exit()
        else:
            print('Информация о пользователе', info.json()['response'][0]['id'], 'получена!')
            logger.info(f'Получение информации о пользователе <requests.get> - {info.status_code}')
            return str(info.json()['response'][0]['first_name'] +'_'+ info.json()['response'][0]['last_name'])

    # Получаем url фото (список словарей с ключами "name", "size", "url")
    def get_url_photos(self, count = 5):
        res = requests.get(self.url, params=self.params)
        logger.info(f'Получение списка фото <requests.get> - {res.status_code}')
        result = res.json()
        json_dict = {}
        json_list = []
        like_list = [] # список лайков
        if 'error' in result.keys(): # проверка наличия прав на альбом
            print(result['error']['error_msg'])
            logger.error(result['error']['error_msg'])
            exit()
        if result['response']['count'] > 0: # провека наличия фото в альбоме
            for i in result['response']['items']:
                size = 0
                if len(json_list) <= count-1:
                    for j in i['sizes']:
                        if j['height']  * j['width'] > size:
                            size = j['height']  * j['width']
                            img_url = j['url']
                            json_dict['size'] = j['type']
                            json_dict['url'] = img_url
                    like = str(i["likes"]['count'])
                    like_list.append(like)
                    if like_list.count(like) > 1:
                        json_dict['name'] = f"{like}-{i['date']}.jpg"
                    else:
                        json_dict['name'] = f"{like}.jpg"
                    json_list.append(json_dict.copy())
                else:
                    break
        else:
            print('в альбоме нет фото!')
            exit()
        print(f"найдено {len(json_list)} фото!")
        return json_list

class YaDisk:
    # получаем список существующих файлов и папок на YaDisk
    def list_dir(self):
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        params = {'path': '/'}
        with open('ya_token.txt') as f:
            self.token = f.read().strip()
        headers = {"Authorization": self.token}
        resp = requests.get(url, params=params, headers=headers)
        logger.info(f'Получение списка существующих файлов и папок на YaDisk <requests.get> - {resp.status_code}')
        ls_dir = []
        for i in resp.json()['_embedded']['items']:
            ls_dir.append(i['name'])
        logger.info(f"Получено {len(ls_dir)} файлов!")
        return ls_dir

    # загрузка файлов на YaDisk
    def up_photos(self, dict, dir, ls_dir):
        # dict - список словарей ключами "name", "size", "url"
        # dir - имя создаваемой папки
        # ls_dir - список существующих файлов и папок на YaDisk
        # запись json-файла:
        dict_json = {} # словарь с ключами "name", "size"
        list_dict_json = [] # список словарей dict_json
        # создание json-файла:
        for i in dict:
            dict_json['file_name'] = i['name']
            dict_json['size'] = i['size']
            list_dict_json.append(dict_json.copy())
        with open("vk.json", "w", encoding="utf-8") as f:
            json.dump(list_dict_json, f, ensure_ascii=False, indent=2)
        # создание папки на YaDisk:
        if dir not in ls_dir:
            url = 'https://cloud-api.yandex.net/v1/disk/resources'
            params = {"path": dir}
            with open('ya_token.txt') as f:
                self.token = f.read().strip()
            headers = {"Authorization": self.token}
            resp = requests.put(url, params=params, headers=headers)
            logger.info(f'Запрос на создание папки на YaDisk <requests.put> - {resp.status_code}')
            if resp.status_code:
                logger.info(f"каталог '{dir}' создан!")
                print(f"каталог '{dir}' создан!")
        else:
            print(f"Каталог {dir} уже существует!")
            logger.info(f"Каталог {dir} уже существует!")
            exit()
        # Загрузка файлов на YaDisk, в созданную папку:
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        for i in dict:
            # Получение ссылки для закачки файла на YaDisk:
            path = f"{dir}/{i['name']}"
            params = {"path": path}
            headers = {"Authorization": self.token}
            resp = requests.get(url, params=params, headers=headers)
            logger.info(f'Получение ссылки для закачки файла на YaDisk <requests.get> - {resp.status_code}')
            url_up = resp.json()['href']
            # Загрузка файла на YaDisk:
            image = requests.get(i['url'])
            up_file = requests.put(url_up, image.content)
            logger.info(f'Загрузка файла на YaDisk <requests.put> - {resp.status_code}')
            if up_file.status_code:
                print(f"файл '{i['name']}' загружен в папку '{dir}'")
                logger.info(f"файл '{i['name']}' загружен в папку '{dir}'")


vk_client = VkUser('552934290') # экземпляр класса VkUser. id - обязательный параметр, album - не обязательный,
# по умолчанию - 'profile' (варианты: 'wall', 'saved')
dir_name = vk_client.user_info() # получаем имя папки "Имя_Фамилия"
img_dict = vk_client.get_url_photos(115) # Сохранить указанное количество фотографий(по умолчанию 5):
up_disk =YaDisk() # экземпляр класса YaDisk
ls_dir = up_disk.list_dir() # список существующих папок и файлов
up_disk.up_photos(img_dict, dir_name, ls_dir) # загрузка файлов на диск