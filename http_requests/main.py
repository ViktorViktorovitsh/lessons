mport requests
from pprint import pprint
import time
from ya_token import TOKEN, GMAIL_PASSWORD  # импорт токена Яндекс и пароля от почты gmail

##########################################################################
#                    парсинг сайта www.reddit.com                        #
#      Скачем гифки на локальный диск, затем загрузим на Яндекс.Диск     #
##########################################################################

# url = "https://http.cat"
url = 'https://www.reddit.com/r/gifs/new.json'

# resp = requests.get(url)
resp = requests.get(url, headers={'User-agent': 'Kei-client'}, params={'limit': 3})  # положим результат запроса в переменную

print(resp)  # сам объект ответа
print("ответ: ", resp.status_code)  # код ответа

# print("заголовок ответа:")
# print(resp.headers)  # заголовки ответа
# print('Content-Type:')
# print(resp.headers['Content-Type'])  # заголовок - словарь, можно обращаться по ключу
# print("байтовое представление:")
# print(resp.content)  # байтовое представление
# resp.encoding = 'utf-8'  # кодировка (опционально)
# print("текстовое представление:")
# print(resp.text)  # текстовое представление (в кодировке UTF-8)
# pprint(resp.json())  # словарь
# print(type(resp.json()))



##########################################################################
#                             вытащим все гифки                          #
##########################################################################

data = resp.json()
print(data['data']['children'][0]['data']['url'])

# все заголовки постов и гифки
posts = data['data']['children']
gif_ls = []
for post in posts:
    title = post['data']['title']  # заголовок поста
    url_gif = post['data']['url']  # ссылка на картинку
    print(title, url_gif)
#     сохраним картинки на диске
    gif_name = url_gif.split('/')[-1]  # выделяем имя из url
    if 'gif' in gif_name:  # отбираем только прямые ссылки
        gif_ls.append(gif_name)  # сохраним имена файлов в список
        with open(gif_name, mode='wb') as file:
            data_gif = requests.get(url_gif)  # получаем гифку по известному url
            file.write(data_gif.content)      # сохраняем в файл (преобразуя объект ответа в бинарный формат)
            print(gif_name, "- OK")
            time.sleep(3)
print(gif_ls)



##########################################################################
#                   Загрузим файлы на ЯндексДиск                         #
##########################################################################

# 1. Получение ссылки для загрузки
# https://yandex.ru/dev/disk/poligon/

url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'  # ссылка из Полигона

for gif in gif_ls:
    # получим ссылку для загрузки
    response = requests.get(url,
                            params={'path': gif},
                            headers={'Authorization': f'OAuth {TOKEN}'})
    print(response.status_code)
    print(response.json())
    href = response.json()['href']  # извлекаем ссылку для загрузки
    print(href)


    # загрузим картинку на ЯДиск
    with open(gif, mode='rb') as f:
        r = requests.put(href, files={'file': f})
    print(r.status_code)




##########################################################################
#                            Работа с API                                #
##########################################################################
"""
stackoverflow -  важный сайт для программистов. И у него есть API. Напишем программу,
которая выводит все вопросы за последние два дня и содержит тэг 'Python'. Токен не требуется.
"""
# import requests
# from datetime import datetime
#
#
# def python_tags(tag):
#     d = datetime.today()  # текущее время
#     to_date = str(round(d.timestamp()))  # текущее время в секундах с начала эпохи.
#     from_date = str(round(d.timestamp() - 259200))  # время в секундах три дня назад
#     url = 'https://api.stackexchange.com/2.2/questions'  # url
#     params = {'fromdate': from_date, 'todate': to_date, 'order': 'desc', 'sort': 'activity', 'tagged': tag,  # параметры запроса
#               'site': 'stackoverflow.com'}
#     resp = requests.get(url, params=params)  # запрос
#     dict_tags = (resp.json())  # результат в словарь
#     # for i in dict_tags['items']:
#     #     print(i['title'])
#     return dict_tags
#
#
# tags = python_tags('python')  # вызываем функцию с параметром "python"
# ls_tags = []
# for i in tags['items']:  # получаем список топиков
#     ls_tags.append(i['title'])
# print(ls_tags)


##########################################################################
#                 отправим результат на почту                            #
##########################################################################
# smtplib — это встроенный модуль Python, предназначенный для отправки писем
# настройки для GMAIL:
# https://support.google.com/a/answer/176600?hl=ru#zippy=%2Cкак-использовать-smtp-сервер-gmail


# import smtplib, ssl
#
# port = 465  # для SSL подключения
# smtp_server = "smtp.gmail.com"  # сервер
# sender_email = "djangotest377@gmail.com"  # Наш емайл (отправителя)
# password = GMAIL_PASSWORD  # Пароль отправителя
# receiver_email = "py.ulgtu@yandex.ru"  # Емайл получателя
# # message = "\n".join(ls_tags)  # отправляемое сообщение
#
# TOPIC = "Вам письмо!"  # заголовок письма
# TEXT = "\n".join(ls_tags)  # отправляемое сообщение  с темой письма
# message = 'Subject: {}\n\n{}'.format(TOPIC, TEXT)
# context = ssl.create_default_context()  # возвращает новый контекст с безопасными настройками по умолчанию,  из библиотеки ssl
# with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:  # запуск безопасного подключения
#     server.login(sender_email, password)  # авторизация на сервере
#     server.sendmail(sender_email, receiver_email, message.encode('utf-8'))  # отправляем письмо, перекодировав текст в UTF-8



##########################################################################
#      вариант 2, менее предпочтительный, за то меньше букв              #
##########################################################################

# import smtplib
# mail_obj = smtplib.SMTP('smtp.gmail.com', 587)  # создаем объект smtplib, дающий доступ к подключению. Первый аргумент - доменное имя, второй – номер порта
# mail_obj.starttls()  # запуск безопасного подключения
# mail_obj.login('djangotest377@gmail.com', GMAIL_PASSWORD)  # авторизация на сервере
# TEXT = "\n".join(ls_tags).encode('utf-8').strip()  # отправляемое сообщение
# mail_obj.sendmail("djangotest377@gmail.com", "py.ulgtu@yandex.ru", TEXT)  # отправляем письмо
# mail_obj.quit()  # если не используется менеджер контекста, то соединение нужно закрыть в ручную
