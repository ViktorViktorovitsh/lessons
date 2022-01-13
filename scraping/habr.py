# Задача: с сайта habr.com извечь только те посты, в которых есть интересные нам хабы(тэги)
# результат - список ссылок

# определяем список хабов, которые нам интересны
DESIRED_HUBS = {'дизайн', 'github', 'физика', 'python'}

import requests
from bs4 import BeautifulSoup

# получаем страницу с самыми свежими постами
url = 'https://habr.com/ru/all/'
response = requests.get(url, headers={'user-agent': 'Agent'})
soup = BeautifulSoup(response.text, 'html.parser')

# извлекаем посты
posts = soup.find_all('article', class_='tm-articles-list__item')  # находим все вхождения (пишем именно class_)
print(len(posts))  # количество постов на странице

for post in posts:
    # print(post.text)
    hubs = post.find_all('span', class_="tm-article-snippet__hubs-item")  # получаем список хабов
    set_hubs = set()
    for hub in hubs:
        set_hubs.add(hub.text.replace('*', '').strip().lower())  # все хабы статьи складываем в сет
        # print(set_hubs)
    if set_hubs & DESIRED_HUBS:  # если есть пересечение с нужными, тогда:
        print(set_hubs & DESIRED_HUBS)
        title_element = post.find('a', class_='tm-article-snippet__title-link')  # сырой заголовок статьи
        print(title_element)
        print(title_element.text)  # название статьи
        print('https://habr.com' + title_element.attrs.get('href'))  # получаем ссылку на статью
        print()

