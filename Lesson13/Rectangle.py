# Создайте класс Rectangle с атрибутами width и height, добавьте метод area(), который возвращает площадь

class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return (1/2) * self.width *self.height

a = Rectangle(6, 4)
print(a.area())