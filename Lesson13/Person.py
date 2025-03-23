# 1. Создайте класс Book с атрибутами title и author.
# Затем создайте объект этого класса и выведите его атрибуты.


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, {self.name}, age {self.age}"


human = Person("Maria", 12)
print(human.greet())