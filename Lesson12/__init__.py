# 1. Создайте класс Book с атрибутами title и author.
# Затем создайте объект этого класса и выведите его атрибуты.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def info(self):
        return f"Book: {self.title} {self.author}"

obj = Book("Holms", "Sir Arthur Conan Doyle")
print(obj.info())

# 2. Создайте класс Dog с атрибутом name.
# Создайте объект класса и измените его атрибут name

class Dog:
    def __init__(self, name = "Dolly"):
        self.name = name

Dog.name = "Masha"
print(Dog.name)

#3. Создайте класс Circle с атрибутом radius и методом, который возвращает длину круга.
# Создайте объект и вызовите метод

import math

class Circle:
    def __init__(self, radius = 6):
        self.radius = radius
        return radius
radius = 6

lenth_circle = ((2 * math.pi) * radius)
print(lenth_circle)

# 4. Создайте класс Laptop с атрибутами brand и price.
# Добавьте метод discount, который уменьшает цену на заданный процент.

class Laptop:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def discount(self):
        percent = 10 / 100
        return self.price * (1 - percent)

product = Laptop("Lee", 199)
print(product.discount())

# 5. Создайте класс Rectangle с атрибутами width и height и методом perimeter,
# который возвращает периметр

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def perimeter(self):
        perimeter = self.width + self.height
        return perimeter

result = Rectangle(6 *2, 8)
print(result.perimeter())

# 6. Создайте класс Student с атрибутами name и grades (список оценок).
# Добавьте метод average_grade, который возвращает среднюю оценку

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def set_grade(self, grades):
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)

pupil = Student("Pupil")
for i in range(1, 7):
    pupil.add_grade(i)
print(pupil.average_grade())

ken = Student("Ken")
ken.set_grade([4, 8, 6, 5, 2])
print(ken.average_grade())

# 7. Создайте класс BankAccount с атрибутами balance и методом deposit, который увеличивает баланс

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self):
        increase = self.balance + int(input())
        return increase

bank = BankAccount(123000)
print(bank.deposit())

# 8. Создайте класс Counter с атрибутом count = 0 и методом increment, который увеличивает count на 1.

class Counter:
    def __init__(self, count = 0):
        self.count = count

    def increment(self):
        augmentation = self.count + 1
        return augmentation
#
# counters = Counter(2)
# print(counters.increment())
#
# 9. Создайте класс Temperature с методом to_fahrenheit, который переводит градусы Цельсия в Фаренгейты.

class Temperature:
    def __init__(self,degree_of_centigrade ):
        self.degree_of_centigrade = degree_of_centigrade

    def to_fahrenheit(self):
        return (self.degree_of_centigrade * 1.8) + 32

tempe = Temperature(23)
print(tempe.to_fahrenheit())

# 10. Создайте класс Converter с методами kg_to_pounds и miles_to_km.






# 12. Создайте класс Employee, который принимает name и salary.
# Добавьте метод info, который выводит данные сотрудника.
#
# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#
#     def info(self):
#         print(self.name, self.salary)
#
# a = Employee("Masha", 5000)
# a.info()
