# 13. Создайте класс Car с атрибутами brand, model и year.
# Создайте несколько объектов с разными значениями

class Car:

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def info(self):
        return self.brand, self.model, self.year

p = Car ("Toyota", "sedan", "2009")
print(p.info())
s = Car("Lada", "sedan", 1999)
print(s.info())
d = Car("Rover", "sedan", 2024)
print(d.info())