import requests
from bs4 import BeautifulSoup
response = requests.get('https://2ip.ru/')  # отправляем запрос, ответ сохраняем в переменной
# print(response.text)

soup = BeautifulSoup(response.text, 'html.parser')  # преобразуем текст в специальный объект, указываем, что работаем с HTML
# print(soup.find(id='d_clip_button').find('span').text)  # найти в супе id, в нем span, в нем текст

# или так
# div = soup.find(id='d_clip_button')
# print(div)  # в блоке кроме IP другого текста нет
# ip = div.text
# print(ip)
print(soup.find(id='d_clip_button').text)