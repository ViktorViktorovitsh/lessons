print('start main')
# import data  # вариант 1
# from data import documents, directories   # вариант 2
# from data import *  # вариант 3
from datapak.data import documents, directories   # вариант 4

class Secretary:
    def __init__(self, login, passwd):
        self.login = login
        self.passwd = passwd

    def shelf(self, dirs):
        availability = False
        num = input('Введите номер документа: ')
        for key in dirs:
            if num in dirs[key]:
                availability = True
                print('Полка №: ', key, '\n')
        if availability == False:
            print('Документ не найден!')

    def ls(self, docs):
        print('Список документов:')
        for doc in docs:
            print(doc['type'], doc['number'], doc['name'])
        print()

    def add(self, docs, dirs):
        new_number = input('Введите номер нового документа: ')
        new_type = input('Введите тип нового документа: ')
        new_name = input('Введите имя: ')
        new_directory = input('Введите номер полки: ')
        if new_directory in dirs.keys():
            new_documents = {}
            new_documents['type'] = new_type
            new_documents['number'] = new_number
            new_documents['name'] = new_name
            docs.append(new_documents)
            dirs[new_directory].append(new_number)
            print('Новые данные внесены!')
        else:
            print('Такой полки не существует')

    def delete(self, docs, dirs):
        availability = False
        num = input('Введите номер документа: ')
        for i, doc in enumerate(docs):
            if num == doc['number']:
                availability = True
                del docs[i]
                print('Документ удален!')
        if availability == True:
            for key in dirs:
                if num in dirs[key]:
                    dirs[key].remove(num)
        else:
            print('Документ не найден!')

    def move(self, dirs):
        num = input('Введите номер документа: ')
        n_dir = input('Введите номер полки: ')
        availability = False
        for val in dirs.values():
            if num in val and n_dir in dirs.keys():
                availability = True
                val.remove(num)
                dirs[n_dir].append(num)
        if availability == False:
            print('Документ или полка не найдены!')
        else:
            print(f"Документ № {num} успешно перемещен на полку {n_dir}!!!\n")

    def add_shelf(self, dirs):
        new_shelf = input('Введите номер новой полки: ')
        if new_shelf not in dirs.keys():
            dirs.setdefault(new_shelf, [])
            print(f"Новая полка № {new_shelf} успешно создана!")
        else:
            print(f"Полка № {new_shelf} уже существует!")

    def people(self, docs):
        num = input('Введите номер документа: ')
        for j in docs:
            if num in j.values():
                print(j['name'])

    def people(self, docs):
        num = input('Введите номер документа: ')
        availability = False
        for doc in docs:
            if num == doc['number']:
                availability = True
                print('Имя: ', doc['name'])
        if availability == False:
            print('Документ не найден!')


def main(docs, dirs):
    secretary = Secretary('Eva', '1234')
    print(f'добрый день, {secretary.login}')
    while True:
        print('Перечень команд:')
        print('d  – удаление документа')
        print('m  - переместить документ')
        print('as - создать новую полку')
        print('p  – кому принадлежит документ')
        print('s  – номер полки c документом')
        print('l  – список всех документов')
        print('a  – добавить новый документ в каталог')
        user_input = input('Введите команду: ')
        if user_input == 'd':
            secretary.delete(docs, dirs)
        elif user_input == 'm':
            secretary.move(dirs)
        elif user_input == 'as':
            secretary.add_shelf(dirs)
        elif user_input == 'p':
            secretary.people(docs)
        elif user_input == 's':
            secretary.shelf(dirs)
        elif user_input == 'l':
            secretary.ls(docs)
        elif user_input == 'a':
            secretary.add(docs, dirs)
        elif user_input == 'q':
            break
        else:
            print('Несуществующая команда!')

        continue

print('значение __name__: ', __name__)

if __name__ == '__main__':
    # main(data.documents, data.directories)  # вариант 1
    main(documents, directories)  # вариант 2, 3, 4
    print('end main')
