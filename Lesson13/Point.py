# 11. Создайте класс Point** с x и y, перегрузите __str__(), чтобы print(Point(1, 2)) выводил "(1, 2)"

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

obj = Point(2, 3)
print(str(obj))