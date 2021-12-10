# создание класса
class MyClass:    # ключевое слово 'class', имя класса в CamelCase
    x = 10        # атрибут класса
    def func():   # атрибут класса (метод)
        print('Hello')

        
# print(MyClass.x)  # вызов атрибута 'x' класса 'MyClass' # 10
# MyClass.func()    # вызов метода 'func' класса 'MyClass'# Hello
# print(type(MyClass)) # <class 'type'> type - это тип всех типов,
#                      # для которых не указан явно иной метакласс



# exemplar = MyClass() # вызывая класс как функцию, запускается конструктор 
# print(exemplar.x)    # 10  # у экземляра класса тоже есть атрибуты
# print(type(exemplar))  # <class '__main__.MyClass'>
# 
# my_list = list()  # это тоже вызов конструктора класса, конструктор - ед. механизм, созд. новые объекты



# Конструктор
# class Register:
#     def __init__(self):  # ф-я __init__ принимает один обязательный аргумент
#                          # - сам экземпляр класса и ничего не возвращает
#         self.regist = 0  # атрибут экземпляра и его значение
#     
#     
# n = Register()
# print(n.regist)
# n.regist += 10
# print(n.regist)



# Коструктор с мн. аргументов
# class Register:
#     def __init__(self, start=1):  # ф-я __init__ может принимать и другие аргументы
#         self.regist = start
#         
# n = Register(10)  # start=10
# print(n.regist)
# n.regist += 10
# print(n.regist)



# Методы
# class Register:
#     def __init__(self):  # ф-я __init__ принимает один обязательный аргумент - сам экземпляр класса и ничего не возвращает
#         self.regist = 0  # атрибут экземпляра и его значение
#     def increment(self): # объявление метода incremen
#         self.regist += 1  
#     def reboot(self):    # self - наш экземпляр, обязательный параметр
#         self.regist = 0
#     
# n = Register()
# print(n.regist)
# n.increment()  # тоже что Register.increment(x) (сязанный метод)
# print(n.regist)
# n.reboot()
# print(n.regist)






# переменные класса и экземпляра
# v1
# class Muzic:
#     tags = []  # атрибут общий для всех экземпляров
#     def __init__(self, artist, track):
#         self.artist = artist  # уникальный атрибут
#         self.track = track
#     def add_tag(self, *args):
#         self.tags.extend(args)
#         
# muzic1 = Muzic('Pain','Call my')
# muzic1.add_tag('Industrial', 'Swеden')      
# muzic2 = Muzic('System Of A Down','Toxicity')
# muzic2.add_tag('Heavi-metal', 'American')
# 
# print(muzic1.artist)
# print(muzic1.tags)




# v2
# class Muzic:
#     
#     def __init__(self, artist, track):
#         self.artist = artist  # уникальный атрибут
#         self.track = track
#         self.tags = []  
#     def add_tag(self, *args):
#         self.tags.extend(args)
#         
# muzic1 = Muzic('Pain','Call my')
# muzic1.add_tag('Industrial', 'Swеden')      
# muzic2 = Muzic('System Of A Down','Toxicity')
# muzic2.add_tag('Heavi-metal', 'American')
# 
# print(muzic1.artist)
# print(muzic1.tags)






# Наследование
class BestList(list):  # наследуемся от класса list (list - класс-родитель, BestList - наследник)
    def even(self):    # добавим метод even
        return len(self) % 2 == 0

ls = BestList()     # создаем экземпляр класа BestList 
ls.extend([1,3,4])  # используем стандартный метод списков, чтобы добавить эл-ты в список
print(ls)           # выглядит как обычный список
print(ls.even())    # а это уже новый, нестандартный метод
ls.append(10)
print(ls.even())

print(isinstance(ls, list))




"""
Класс Products, в котором есть атрибуты: наименование, цена, запасы на складе.
prod_info - печатает информацию о товаре
rub_conv - переводит цену в рубли
"""

# class Products:
#     def __init__(self, name = 'new product', price = 0.99, in_stock = 0):        
#         self.price = price
#         self.name = name
#         self.in_stock = in_stock
#     def prod_info(self):
#         print(self.name)
#         print(self.price)
#         print(self.in_stock)
#     def rub_conv(self):
#         print(self.price * 75, 'rub')
# 
# 
# apple = Products()
# print(apple.name)
# apple.prod_info()
# print()
# 
# orange = Products('Orange Tunis', 5.0, 1000)
# orange.prod_info()
# print()
# 
# cherry = Products()
# cherry.name = 'cherry Egypt'
# cherry.price = 7.5
# cherry.in_stock = 500
# print(cherry.name)
# print(cherry.price)
# print(cherry.in_stock)
# cherry.rub_conv()






"""
Класс Student, в котором есть три атрибута: name, groupNumber и age.
По умолчанию name = Ivan, age = 18, groupNumber = 10A.
В классе реализовано пять методов:
get_name - для получения данных об имени конкретного студента
get_age - для получения данных о возрасте конкретного студента
get_group - для получения данных о номере группы конкретного студента
set_name - позволяет изменить имя студента
set_group - позволяет изменить группу студента
"""

# class Student():
#     def __init__(self, name = "no_name", age = 18, group = None): 
#         self.name = name
#         self.age = age
#         self.group = group
#     def get_name(self):
#         return self.name
#     def get_group(self):
#         return self.group
#     def get_age(self):
#         return self.age    
#     def set_name(self, name):
#         self.name=name
#         return self.name
#     def set_age(self, age):
#         self.age=age
#         return f"возраст студента {age} лет"
#     def set_group(self,group):
#         self.group = group
#         return f"группа студента {group}"
#  
# egor = Student("Егор Летов", 20, "Пдо-33")
# print(egor.name, egor.age, egor.group, '\n')
# 
# yana = Student()
# print(yana.name)
# print(yana.group, '\n')
# yana.set_name("Яна Дягилева")
# yana.set_age(25)
# yana.set_group('Пдо-44')
# print(yana.name, yana.age, yana.group, '\n')
# 
# print(egor.get_name())
# print(yana.get_group())




