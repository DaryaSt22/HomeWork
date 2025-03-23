# Создайте класс MathUtils с методом is_even(n), который возвращает True, если
# число четное.

class MathUtils:

    def __init__(self, number):
        self.number = number

    def is_even(self):
        return self.number % 2 == 0

num = MathUtils(25)
print(num.is_even())
