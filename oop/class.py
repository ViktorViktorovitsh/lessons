"""
Задача № 1
Напишите программу с классом Calc. Создайте два атрибута — a и b. Напишите методы addition — сложение,
multiplication — умножение, division — деление, subtraction — вычитание.
При передаче в методы параметров a и b с ними нужно производить соответствующие действия и печатать ответ.

Задача № 2
Напишите программу с классом Car. Создайте конструктор класса Car. Создайте атрибуты класса Car — color (цвет),
type (тип), year (год). Напишите пять методов.
Первый — запуск автомобиля, при его вызове выводится сообщение «Автомобиль заведен».
Второй — отключение автомобиля — выводит сообщение «Автомобиль заглушен».
ретий — присвоение автомобилю года выпуска. Четвертый метод — присвоение автомобилю типа.
Пятый — присвоение автомобилю цвета.

Задача № 3
Напишите программу с классом Triangle, принимающий три значения длин отрезков.
Напишите Метод is_triangle() и возвращающий результат(True, False) в зависимости от того
можно ли из этих отрезков построить треугольник.
"""

# Задача № 1
class Calc:
    def __init__(self, a, b):
        self.a = a  
        self.b = b
    def addition(self):
        return self.a + self.b
    def multiplication(self):
        return self.a * self.b    
    def division(self):
        return self.a / self.b
    def subtraction(self):
        return self.a - self.b    

# x = Calc(3, 7)
# print(x.b)
# print(x.addition())
# print(x.multiplication())
# print(x.division())
# print(x.subtraction())

# Задача № 2
class Car:
    def __init__(self, color = 'red', form = 'sedan', year = '2020'):
        self.color = color  
        self.form = form
        self.year = year
    def run(self):
        print('Автомобиль заведен')
    def set_year(self, y):
        self.year = y
    

# vaz = Car()
# vaz.color = 'black'
# print(vaz.color)
# vaz.run()
# vaz.set_year('2021')
# print(vaz.year)

class Car:
    def run(self):
        print('Автомобиль заведен')
 

# audi = Car()
# audi.color = 'green'
# audi.form = 'hatchback'
# audi.year = 2020
# print(audi.color, audi.form, audi.year)
# audi.run()

# abn912 = ProductInStore()
# abn912.name = 'Anakin action figure 921'
# abn912.price = 56.11
# abn912.qty_in_stock = 11
# print abn912.name, abn912.price, abn912.qty_in_stock



# Задача № 3
class Triangle:
    def __init__(self, sides):
        self.sides = sides

    def is_triangle(self):
        if all([side > 0 for side in self.sides]):
            for side in self.sides:
                sorted_sides = sorted(self.sides)
                if sorted_sides[0] + sorted_sides[1] > sorted_sides[2]:
                    return True
                else:
                    return False
        else:
            return 'Стороны должны быть положительными'
   
        
triangle1 = Triangle([2, 3, 4])
print(triangle1.is_triangle())
triangle2 = Triangle([77, 3, 4])
print(triangle2.is_triangle())
triangle3 = Triangle([6, -3, 4])
print(triangle3.is_triangle())

