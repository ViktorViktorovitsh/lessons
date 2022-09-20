from pprint import pprint

#цикл while

# x = 10
# while x > 0:
#   print(x, end=" ")
#   x -= 1   # x = x -1



# x = 10
# while x > 0:
#   if x % 2 == 0:
#     print(x, 'четное число')
#   else:
#     print(x, 'нечетное число')
#   x -= 1


# вечный цикл
# x = 10
# while x > 0:
#   print(x)

# исправляем вечный цикл
# x = 100
# while True:
#   print(x)
#   x -= 1
#   if x < 0:
#     break


# while True:
#     name = input("Введите свое имя: ")
#     if name == "admin":
#         print("Welcome!")
#         break
#     else:
#         print("Доступ запрещен!")


# цикл for
nekrasov = 'Однажды в студёную зимнюю пору, я из лесу вышел, был сильный мороз...'
# for i in nekrasov:
#     print(i)

# break, continue, pass
# for letter in nekrasov:
#     if letter == 'ё':
# #       break
# #       continue
#       pass
#     print(letter, end="")   
# print()



    
# enumerate() — это встроенная функция в Python, которая позволяет вам иметь автоматический счетчик во время цикла по итерациям. 
# Функция enumerate() принимает следующий вид: enumerate(iterable, start=0)
# Функция принимает два аргумента: iterable — объект, поддерживающий итерацию. start — число, с которого начинается счетчик (по умолчанию start = 0)
# возвращает индекс и элемент объекта

# Напечатаем только нечетные символы
# for i, simbol in enumerate(nekrasov, 1):
#     if i % 2 != 0:
#         print(i, simbol, end = " ")



## функция range возвращает итерируемый объект, принимать может три параметра (int): старт, стоп, шаг
# по объекту типа range можно итерироваться как по списку

# print(list(range(10)))
# print(type(range(10)))

# for num in range(1, 10, 3):
#   print(num, end = ' ')



## факториал 
# n = 10000
# fact = 1
# for i in range(1, n + 1):
#   fact = fact * i
# 
# print(len(str(fact)))

# Вложенный цикл
# Таблица умножения
# for i in range(1, 10):
#     for j in range(1, 10):
#         print(i * j, end=" ")
#     print()
# print()    
    
  
# Таблица умножения v2   
# for i in range(1, 10):
#     for j in range(1, 10):
#         res = str(i * j)
#         if len(res) < 2:
#             res = " " + res
#         print(res, end=" ")
#     print()



# n_start = 1
# n_end = 10000
# ls_simple = []
# for number in range(n_start, n_end + 1):
#     ls_div = list()
#     for div in range(1, number + 1):
#         if number % div == 0:
#             ls_div.append(div)
# #             print(number, div)
#     if len(ls_div) < 3:
#         ls_simple.append(number)
# print(ls_simple[-1])


