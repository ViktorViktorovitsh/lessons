import csv
from pprint import pprint
# чтение csv-файла в список
print('чтение csv-файла')
with open('users.csv') as f:   # открываем файл в режиме чтения
    reader = csv.reader(f, delimiter=",")     # создаем объект csv.reader (возвращает итератор)
    for row in reader:         # вывод на экран элемнетов ридера с помощь цикла
        print(row)

# # получаем список
with open('users.csv') as f:   # открываем файл в режиме чтения
    reader = csv.reader(f)     # создаем объект csv.reader (возвращает итератор)
    data = list(reader)        # Десериализация в список
print()
pprint(data)



print()
with open('users.csv') as f:   # превращаем csv.reader в список
    reader = csv.reader(f)
    ls_users = list(reader)
print(ls_users)

print()
ls_users.pop(0)  # удаляем названия столбцов
ls_users.pop(-1)
print(ls_users)




# тоже самое используя встроенные ф-и
print()
with open('users.csv') as f:   # превращаем csv.reader в список
    ls = f.readlines()
    
ls_users2 = []
for i in ls:
    ls_users2.append(i.strip().split(','))
    
print(ls_users2)




# чтение csv-файла в словарь
print('\n', 'чтение csv-файла в словарь')
ls_dict = []
with open('users.csv') as f:
    reader = csv.DictReader(f)  # используем метод DictReader(возвращает объект чтения)
    for line in reader:
        print(line)
        print(line['name'])
        ls_dict.append(line)
   
print('\n', reader, '\n')
pprint(ls_dict)



# # Запись  
users_data = [
    ['lori49@gmail.com', 'Victor', 'Webb', '20:07:1996', 'male'],
    ['rodriguezbryan@gmail.com', 'Patrick', 'Logan', '17:08:1998', 'male'],
    ['troyjones@gmail.com', 'Megan', 'Yates', '19:08:1998', 'female'],
    ['shannon51@gmail.com', 'Geoffrey', 'Kent', '16:05:1995', 'male'],
    ['marymills@gmail.com', 'Travis', 'Allen', '12:05:1997', 'male'],
    ['dillon67@gmail.com', 'Courtney', 'Soto', '04:07:1996', 'female'],
    ['kellypalmer@gmail.com', 'Matthew', 'Wright', '05:10:1998', 'male'],
    ['jamesmartha@gmail.com', 'Amy', 'Chavez', '04:04:1998', 'female'],
    ['walshmorgan@gmail.com', 'Jennifer', 'Jones', '11:04:1998', 'female'],
    ['olivia45@gmail.com', 'Paul', 'Santiago', '19:05:1996', 'male'],
    ['dianecantrell@gmail.com', 'Anita', 'Davis', '04:02:1997', 'female'],
    ['courtney10@gmail.com', 'Samuel', 'James', '15:01:1995', 'male'],
    ['diamond36@gmail.com', 'George', 'Barry', '27:03:1996', 'male'],
    ['stephanie54@gmail.com', 'Matthew', 'Montgomery', '03:01:1996', 'male'],
    ['catherinebright@gmail.com', 'Joshua', 'Chang', '07:04:1998', 'male'],
    ['castrobryan@gmail.com', 'Christopher', 'White', '02:11:1996', 'female'],
    ['jessica39@gmail.com', 'Lori', 'Byrd', '10:02:1997', 'female'],
    ['andersondavid@gmail.com', 'Andrew', 'Williams', '19:04:1996', 'male'],
    ['rhall@gmail.com', 'Abigail', 'Peters', '23:08:1995', 'female'],
    ['hlopez@gmail.com', 'Julie', 'Jacobs', '13:07:1996', 'female']
]

# writerow
print('\n', 'writerow: ')
with open('users_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for line in users_data:
        print(line)
        writer.writerow(line)
print()
with open('users_data.csv') as f:
    print(f.read())


# writerows
print('\n', 'writerows: ')
with open('users_data2.csv', 'w', newline='') as f:
    writer = csv.writer(f, delimiter=";")
    writer.writerows(users_data)

with open('users_data2.csv') as f:
    print(f.read())


# json
import json
from pprint import pprint

# чтение
with open('response.json', encoding='utf-8') as f:
    data = json.load(f)
pprint(data)




# запись
user = {'name': 'Jessica', 'last_name': 'James', 'age': '21'}

with open('users.json', 'w') as f:
    f.write(json.dumps(user))

with open('users.json') as f:
    print(f.read())



with open('users2.json', 'w') as f:
    json.dump(user, f)
with open('users2.json') as f:
    print(f.read())

with open('cp1251.txt') as f:
    print(f.read())
# # 
with open('utf8.txt', encoding='utf-8') as f:
    print(f.read())




