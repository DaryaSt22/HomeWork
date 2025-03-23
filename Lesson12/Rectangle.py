# 5. Создайте класс Rectangle с атрибутами width и height и методом perimeter,
# который возвращает периметр

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def perimeter(self):
        return (self.width + self.height)*2

result = Rectangle(6, 8)
print(result.perimeter())