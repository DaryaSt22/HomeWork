# 10. Создайте класс Counter, который хранит число и имеет методы increase() и
# decrease()

class Counter:
    def __init__(self):
        self.number = 2

    def increase(self):
        self.number += 1

    def decrease(self):
        self.number -= 1

cont = Counter()
print(cont.number)
cont.increase()
print(cont.number)
cont.decrease()
print(cont.number)
