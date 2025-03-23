# 8. Создайте класс Counter с атрибутом count = 0 и методом increment, который увеличивает count на 1.

class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count =  self.count + 1

counters = Counter()
print(counters.count)
counters.increment()
print(counters.count)