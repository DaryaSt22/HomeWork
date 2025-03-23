# 14. Создайте класс Math, содержащий метод add(a, b), который складывает два числа.

class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        if isinstance(other, Math):
            return Math(self.a + self.other and self.b + self.other)
        raise TypeError("Можно складывать только с другим объектом CustomList")

summa1 = Math(22, 22)
summa2 = Math(10, 10)
summa3 = summa1 + summa2

print(summa3.__add__())