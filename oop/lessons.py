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









