#3. Создайте класс Circle с атрибутом radius и методом, который возвращает длину круга.
# Создайте объект и вызовите метод

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def length_circle(self):
        return (2 * math.pi) * self.radius

obj = Circle(6)
print(obj.length_circle())