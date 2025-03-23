# 6. Создайте класс Circle, который принимает радиус и имеет метод circumference(),
# возвращающий длину окружности

import math
class Circle:

    def __init__(self, radius):
        self.radius = radius

    def circumference(self):
        return 2 * math.pi * self.radius

c = Circle(6)
print(c.circumference())