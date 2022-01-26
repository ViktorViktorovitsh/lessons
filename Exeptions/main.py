# Обработка исключений в Python
# Попытка деления на 0
x = 10 / 0
print(x)


# Обработаем исключение
# try:
#     x = 10 / 0  # В этом блоке могут быть ошибки
# except ZeroDivisionError:
#     x = None    # выполняется, если блок try выбрасывает ошибку
# else:
#     print('Ошибок нет')  # выполняется, если в блоке try нет ошибок
# finally:
#     print(x)    # Этот блок выполняется всегда
  
  
  
# Или так:
# try:
#     x = 10 / 0
# # except:  # так лучше не делать
# except ZeroDivisionError:
#     x = None
# print(x)


# ValueError
# try:
#     x = float(input("Введите число: "))
# except ValueError:
#     print("Введено не число!")
# else:
#     print("Введено число: ", x)
# print("Завершение программы")



# # еще пример
# print("Старт программы")
# try:
#     print("Открываем файл...")
#     f = open("data.txt", "r")
#     lines = f.readlines()
#     print(lines[1])
# except FileNotFoundError:
#     print("Файл не найден!")
# except IndexError:
#     print('нет такой строки!')
# else:
#     print("Закрываем файл...")
#     f.close()
# finally:
#     f.close()
# if f.closed:
#     print('файл закрыт!')
# print("Программа завершена")




# # Несколько блоков except
# print("Program started")
# try:
#     a = int(input("Введите число а: "))
#     b = int(input("Введите число b: "))
#     print(a/b)
# except ValueError:
#     print("Введено не число!")
# except ZeroDivisionError as zde:
#     print("На 0 делить нельзя!")
#     print(zde)   # передача сообщения об ошибке (аргумента исключения)
# print("Program finished")
#     



# # raise
# age = int(input('Введите свой возраст: '))
# age = -100
# if age < 0:
#     raise ValueError('Возраст может быть только положительным!!!')
# print(age)





# # Создание собственных исключений
# class MyError(Exception):
#     """
#     custom exception
#     """
#
# age = -55
# if age < 0:
#     raise MyError('Моя ошибка')




# class MyError(Exception):
#     def __init__(self, text):
#         self.txt = text
#         
# try:
#     raise MyError('Моя ошибка')
# except MyError as er:
#     print(er)



# from math import sqrt2
# x = input('Введите число: ')
# print('Корень числа:', sqrt(x))

# def division():
#     nums = input('Введите два числа через пробел: ').split()
#     return float(nums[0]) / float(nums[1])
#
# division()


# age = float(input('введите возраст: '))
# if age < 0:
#     raise Exception('Возраст должен быть больше нуля!')

