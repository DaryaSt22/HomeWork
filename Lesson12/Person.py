# 11. Создайте класс Person, который принимает name и age в конструкторе.
# Создайте объект и выведите его данные

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Имя: {self.name}, Возраст: {self.age}")

obj1 = Person("Vasya", 55)
obj1.display()