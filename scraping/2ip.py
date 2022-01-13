# Парсинг сайта 2ip.ru
# Узнаем свой IP

import requests
response = requests.get('https://2ip.ru')  # отправить запрос, сохранить ответ
# print(response)

if not response.ok:  # проверяем валидность ответа
    raise Exception('Неравильный ответ')

text = response.text  # получаем текст разметки
# print(text)
div_pos = text.find('id="d_clip_button')  # получаем индекс блока div с нужным идентификатором
print(div_pos)
span_pos = text.find('<span>', div_pos)   # получаем индекс блока span, следующего за идентификатором
print(span_pos)
span_pos_end = text.find('</span>', span_pos)   # получаем индекс конца блока span
print(span_pos_end)
ip = text[span_pos+6:span_pos_end]  # получаем ip
print(ip)