# 15. Создайте класс Counter, который содержит атрибут класса total = 0.
# Увеличивайте total при вызове метода Increase

class Counter:
    def __init__(self, total = 0):
        self.total = total

    def increase(self):
        return self.total + 1

p = Counter(2)
print(p.increase())