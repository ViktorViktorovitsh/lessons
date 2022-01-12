import requests
from pprint import pprint

# url = "https://http.cat"
url = 'https://www.reddit.com/r/gifs/new.json'

# resp = requests.get(url)
resp = requests.get(url, headers={'User-agent': 'Kei-client'}, params={'limit': 5})  # положим результат запроса в переменную

print(resp)  # сам объект ответа
print(resp.status_code)  # код ответа
# print(resp.headers)  # заголовки ответа
# print(resp.headers['Content-Type'])  # заголовок - словарь, можно обращаться по ключу
# print(resp.content)  # байтовое представление
# resp.encoding = 'utf-8'  # кодировка (опционально)
# print(resp.text)  # текстовое представление (в кодировке UTF-8)
# pprint(resp.json())  # словарь
# print(type(resp.json()))


# вытащим все гифки
data = resp.json()
print(data['data']['children'][0]['data']['url'])


# все заголовки постов и гифки
posts = data['data']['children']
for post in posts:
    title = post['data']['title']  # заголовок поста
    url_gif = post['data']['url']  # ссылка на картинку
    print(title, url_gif)
    # сохраним картинки на диске
    # gif_name = url_gif.split('/')[-1]  # выделяем имя из url
    # if 'gif' in gif_name:  # отбираем только прямые ссылки
    #     with open(gif_name, mode='wb') as file:
    #         data_gif = requests.get(url_gif)  # получаем гифку по известному url
    #         file.write(data_gif.content)      # сохраняем в файл (преобразуя объект ответа в бинарный формат)





# Загрузим файлы на ЯндексДиск
# 1. Получение ссылки для загрузки
# https://yandex.ru/dev/disk/poligon/

url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'  # ссылка из Полигона
with open('token.txt') as f:  # получаем токен из файла
    token = f.read().strip()

# получим ссылку для загрузки
response = requests.get(url,
                        params={'path': 'file.gif'},
                        headers={'Authorization': f'OAuth {token}'})
print(response.status_code)
print(response.json())
href = response.json()['href']  # извлекаем ссылку для загрузки
print(href)


# загрузим картинку на ЯДиск
with open('s2f4ds6r37b81.gif', mode='rb') as f:
    r = requests.put(href, files={'file': f})
print(r.status_code)


