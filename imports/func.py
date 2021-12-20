from pprint import pprint

documents = [
    {"type": "diplom", "number": "112233", "name": "Илон Маск"},
    {"type": "medical_book", "number": "1234", "name": "Илон Маск"},
    {"type": "insurance", "number": "100", "name": "Илон Маск"},
    {"type": "diplom", "number": "333555", "name": "Билл Гейтс"},
    {"type": "medical_book", "number": "2222", "name": "Билл Гейтс"},
    {"type": "diplom", "number": "778899", "name": "Линус Торвальдс"},
    {"type": "insurance", "number": "333", "name": "Линус Торвальдс"},
]

directories = {
    '1': ['112233', '333555', '778899'],
    '2': ['1234', '2222'],
    '3': ['100', '333']
}


def shelf(dirs):
    availability = False
    num = input('Введите номер документа: ')
    for key in dirs:
        if num in dirs[key]:
            availability = True
            print('Полка №: ', key, '\n')
    if availability == False:
        print('Документ не найден!')


def ls(docs):
    print('Список документов:')
    for document in documents:
        print(document['type'], document['number'], document['name'])
    print()


def add(docs, dirs):
    new_number = input('Введите номер нового документа: ')
    new_type = input('Введите тип нового документа: ')
    new_name = input('Введите имя: ')
    new_directory = input('Введите номер полки: ')
    if new_directory in directories.keys():
        new_documents = {}
        new_documents['type'] = new_type
        new_documents['number'] = new_number
        new_documents['name'] = new_name
        docs.append(new_documents)
        dirs[new_directory].append(new_number)
        print('Новые данные внесены!')
    else:
        print('Такой полки не существует')


def delete(docs, dirs):
    availability = False
    num = input('Введите номер документа: ')
    for i, doc in enumerate(docs):
        if num == doc['number']:
            availability = True
            del docs[i]
            print('Документ удален!')
    if availability:
        for key in dirs:
            if num in dirs[key]:
                dirs[key].remove(num)
    else:
        print('Документ не найден!')


def move(dirs):
    num = input('Введите номер документа: ')
    n_dir = input('Введите номер полки: ')
    availability = False
    for val in dirs.values():
        if num in val and n_dir in dirs.keys():
            availability = True
            val.remove(num)
            dirs[n_dir].append(num)
    if not availability:
        print('Документ или полка не найдены!')
    else:
        print(f"Документ № {num} успешно перемещен на полку {n_dir}!!!\n")


def add_shelf(dirs):
    new_shelf = input('Введите номер новой полки: ')
    if new_shelf not in dirs.keys():
        dirs.setdefault(new_shelf, [])
        print(f"Новая полка № {new_shelf} успешно создана!")
    else:
        print(f"Полка № {new_shelf} уже существует!")


def people():
    num = input('Введите номер документа: ')
    for j in documents:
        if num in j.values():
            print(j['name'])


def people(docs):
    num = input('Введите номер документа: ')
    availability = False
    for doc in docs:
        if num == doc['number']:
            availability = True
            print('Имя: ', doc['name'])
    if availability == False:
        print('Документ не найден!')


def main(docs, dirs):
    while True:
        #     print('Документы на полках: ')
        #     print(directories)
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
            delete(docs, dirs)
        elif user_input == 'm':
            move(dirs)
        elif user_input == 'as':
            add_shelf(dirs)
        elif user_input == 'p':
            people(docs)
        elif user_input == 's':
            shelf(dirs)
        elif user_input == 'l':
            ls(docs)
        elif user_input == 'a':
            add(docs, dirs)
        elif user_input == 'q':
            break
        else:
            print('Несуществующая команда!')

        continue


main(documents, directories)
print()
pprint(documents)
print()
print(directories)
