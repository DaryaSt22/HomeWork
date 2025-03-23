# 3. Создайте класс Car с атрибутами brand, model и year, добавьте метод full_info(),
# который возвращает строку с полной информацией

class Car:

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def full_info(self):
        return f"Бренд: {self.brand}, модель: {self.model}, год: {self.year}"

a = Car("Volvo", "sedan", 2025)
print(a.full_info())