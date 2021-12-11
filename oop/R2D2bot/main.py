from vk_api.longpoll import VkLongPoll, VkEventType
from random import randrange
import requests
import vk_api
from datetime import date
from pprint import pprint
import db

# Токен сообщества
group_token = 'токен сообщества'

# Токен пользователя
user_token = 'токен пользователя'

# Авторизуемся как сообщество
vk = vk_api.VkApi(token=group_token)

# Активируем "длинные" запросы
longpoll = VkLongPoll(vk)

# Функция отправки сообщения
def send_msg(user_id, message, attachment=''):  # 2.3  
    vk.method('messages.send', {'user_id': user_id, 'message': message,
                                'random_id': randrange(10 ** 7), 'attachment': attachment})

class R2D2_bot: # основной класс
    def __init__(self, user_id):
        self.user = db.User
        self.user_id = user_id 
        self.offset = 0  # Смещение относительно первого найденного пользователя 
        
    # Получаем имя, фамилию и др. данные пользователя
    def get_user_name(self): 
        self.user_params = {}
        self.params = {'access_token': user_token,
            'v': '5.131',
            'user_ids': self.id,
            'fields': 'sex, bdate, city, country'}    
        response = requests.get('https://api.vk.com/method/users.get', self.params)
        for user_info in response.json()['response']:
            self.user_params.update(first_name = user_info['first_name'])
            self.user_params.update(last_name = user_info['last_name'])
            today = date.today()
            if 'bdate' in user_info:
                if len(user_info['bdate'].split('.')) == 3: # проверяем что указан год рождения
                    age_str = today.year - int(user_info['bdate'].split('.')[2]) 
                    self.user_params.update(age = age_str)
                else:
                    self.user_params.update(age = None) # если не указан год, то None
            if 'city' in user_info:
                self.user_params.update(city = user_info['city']['title'])
                self.city = user_info['city']['id']
            else:
                send_msg(self.user_id, 'В профиле не указан город, введите название города')
                for new_event in longpoll.listen():
                    if new_event.type == VkEventType.MESSAGE_NEW and new_event.to_me: 
                        response = requests.get('https://api.vk.com/method/database.getCities',
                            {'access_token': user_token, 'v': '5.131', 'country_id': 1, 'count': 1, 'q': new_event.message}) 
                        self.city = response.json()['response']['items'][0]['id']
                        self.user_params.update(city = response.json()['response']['items'][0]['title'])
                        break         
                       
            if 'sex' in user_info:
                self.user_params.update(sex = user_info['sex'])      
        return self.user_params

    # Отправка сообщений ботом
    def new_message(self, message):      
        if message.lower() == 'привет':
            return 'Привет! Для старта, отправьте "С"'

        # Старт
        elif message.lower() == 'с':
            send_msg(self.user_id, 'Введите свой id')
            for new_event in longpoll.listen():
                if new_event.type == VkEventType.MESSAGE_NEW and new_event.to_me:
                    self.id = int(new_event.message.lower())
                    break          
            return self.bot_menu()

        # Выход
        elif message.lower() == 'q':
            return self.bot_menu()

        # Неизвестное боту сообщение
        else:
            return 'Не понял, повторите'

    # Получаем параметры поиска 
    def start(self): # 2
        self.get_user_name() # Получаем имя юзера и др.
        db.create_tables()
        self.user = db.User(vk_id = self.id, first_name=self.user_params['first_name'], last_name=self.user_params['last_name'],
            range_age=self.user_params['age'], city=self.city)
        if not db.check(self.id):
            db.add_user(self.user)  # добавляем запись в таблицу 'User'
        else:
            self.user.id = db.check(self.id)
        sity = self.user_params['city']
        if self.user_params['sex'] == 1:  
            sex = 'женский' 
            self.sex = 2 
        else:
            sex = 'мужской'
            self.sex = 1
        
        send_msg(self.user_id, f'Привет, {self.user_params["first_name"]}')
        send_msg(self.user_id, f'Ваш город: {sity}')
        send_msg(self.user_id, f'Ваш пол: {sex}')
        send_msg(self.user_id, f'Начинаем поиск? (Д / Н)')
        for new_event in longpoll.listen():
            if new_event.type == VkEventType.MESSAGE_NEW and new_event.to_me: 
                if new_event.message.lower() == 'д':
                    self.get_age()
                    self.find_user_data()
                    self.get_photos()
                    send_msg(self.user_id, 
                        f'Имя: {self.first_name}\n'
                        f'Фамилия: {self.last_name}\n Профиль: https://vk.com/id{self.dating_user_id}',
                        self.top_photos)
                    return self.find_half()
                else:
                    return self.bot_menu()

    # Меню бота
    def bot_menu(self): 
        """
        Главное меню. Навигация:
        В - вывести базу;
        Н – новый поиск;   
        Q - завершить работу
        """
        send_msg(self.user_id, self.bot_menu.__doc__)
        while True:
            for new_event in longpoll.listen():
                if new_event.type == VkEventType.MESSAGE_NEW and new_event.to_me:
                    if new_event.message.lower() == 'в':
                        send_msg(self.user_id, 'Вы добавили следующих людей в базу:')
                        dating_users = db.view_all(self.id)
                        for dating_user in dating_users:
                            send_msg(self.user_id, f'https://vk.com/id{dating_user}')
                        send_msg(self.user_id, self.bot_menu.__doc__)

                    # Новый поиск
                    elif new_event.message.lower() == 'н':
                        self.offset = 0
                        self.start()

                    # Выход
                    elif new_event.message.lower() == 'q':
                        return exit()

                    # Неизвестное сообщение
                    else:
                        send_msg(self.user_id, 'Не понял, повторите')

    # Поиск юзера 
    def find_user_data(self): 
        self.params = {'access_token': user_token,
                'v': '5.131',
                'count': 1,
                'offset': self.offset,
                'city': self.city,
                'country': 1, 
                'sex': self.sex,
                'age_from': self.age_from,
                'age_to': self.age_to,
                'fields': 'is_closed',
                'status': 6,  # в активном поиске
                'has_photo': 1} # только с фото
        response = requests.get('https://api.vk.com/method/users.search', self.params)
        if response.json()['response']['items']:
            for dating_user_id in response.json()['response']['items']:
                private = dating_user_id['is_closed']
                if private:
                    print('private')
                    self.offset += 1
                    self.find_user_data()
                else:
                    print('not private')
                    self.dating_user_id = dating_user_id['id']
                    print(self.dating_user_id)
                    self.first_name = dating_user_id['first_name']
                    self.last_name = dating_user_id['last_name']
                    # проверим наличие кандидата в базе, если есть - игнорим
                    if db.check_half(self.dating_user_id):
                        self.offset += 1
                        self.find_user_data()
        else:
            print('not response')
            self.offset += 1
            self.find_user_data()

    def find_half(self): 
        send_msg(self.user_id, 'Добавить в базу? (Д / Н)')
        send_msg(self.user_id, 'Выход - "Q"')
        while True:
            for new_event in longpoll.listen():
                if new_event.type == VkEventType.MESSAGE_NEW and new_event.to_me:
                    if new_event.message.lower() == 'д':

                        dating_user = db.DatingUser(vk_id=self.dating_user_id, first_name=self.first_name,
                                                    last_name=self.last_name, id_User=self.user.id, Like = True)
                        db.add_user(dating_user) # добавляем запись в таблицу 'DatingUser'
                        send_msg(self.user_id, 'Пользователь добавлен в базу, продолжить?')
                        for new_event in longpoll.listen():
                            if new_event.type == VkEventType.MESSAGE_NEW and new_event.to_me:
                                if new_event.message.lower() == 'н':
                                    return self.bot_menu()
                                else:
                                    return self.find_item()
                    elif new_event.message.lower() == 'н':
                        dating_user = db.DatingUser(vk_id=self.dating_user_id, first_name=self.first_name,
                                                    last_name=self.last_name, id_User=self.user.id, Like = False)
                        db.add_user(dating_user) # добавляем запись в таблицу 'DatingUser'
                        return self.find_item()
                    elif new_event.message.lower() == 'q':
                        return self.bot_menu()
                    else:
                        self.find_item()

    def find_item(self):
        send_msg(self.user_id, 'Ищем дальше')
        self.offset += 1
        self.find_user_data()
        self.get_photos()
        send_msg(self.user_id, f'Имя: {self.first_name}\n'
                                f'Фамилия: {self.last_name}\n Профиль: https://vk.com/id{self.dating_user_id}',
                    self.top_photos)
        return self.find_half()

    # Возрастной диапазон
    def get_age(self): 
        send_msg(self.user_id, 'Введите возрастной диапазон через пробел, например, "22 33"')
        for new_event in longpoll.listen():
            if new_event.type == VkEventType.MESSAGE_NEW and new_event.to_me:
                try:
                    self.age_range = new_event.message.split(' ')                
                    self.age_range = [int(i) for i in self.age_range]
                    if self.age_range[0] >= 18:
                        self.age_from = self.age_range[0]
                        self.age_to = self.age_range[1]
                        return self.age_range                    
                    else:
                        send_msg(self.user_id, 'Неправильно введён диапазон. Пожалуйста, повторите ввод.')               
                except:
                    send_msg(self.user_id, 'Неправильно введён диапазон. Пожалуйста, повторите ввод.')

    # Получаем фото пользователя
    def get_photos(self):
        photos = []
        response = requests.get(
            'https://api.vk.com/method/photos.get',
                    {'access_token': user_token,
                    'v': '5.131',     
                    'owner_id': self.dating_user_id,
                    'album_id': 'profile', 
                    'extended': 1, # доп. поля (лайки)
                    'count': 1000}  # max количество записей, которое будет получено
                    )
        try:
            sorted_response = sorted(response.json()['response']['items'], key=lambda x: x['likes']['count']) # сортировка по лайкам
            for photo_id in sorted_response:
                photos.append(f"photo{self.dating_user_id}_{photo_id['id']}")
            self.top_photos = ','.join(photos[-3:]) # оставляем 3 фото 
            return self.top_photos
        except:
            pass

if __name__ == '__main__':
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            bot = R2D2_bot(event.user_id) 
            send_msg(event.user_id, bot.new_message(event.text))