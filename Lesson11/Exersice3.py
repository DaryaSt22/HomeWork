class  Car:

# Реализовать пять методов.

    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

#  Запуск автомобиля – выводит строку «Автомобиль заведён»

    def start(self):
        print("Автомобиль заведён")

    # Отключение автомобиля – выводит строку «Автомобиль заглушен».

    def disconnection(self):
        print("Автомобиль заглушен")

    def set_description(self):
        return f"{self.color}"

    def set_sedan(self):
        return f"{self.type}"

    def set_enter(self):
        return f"{self.year}"

# Методы для присвоения автомобилю года выпуска, типа и цвета.

desc = Car("красный", "sedan", "2025")

print("Цвет машины: ", desc.get_description())
print("Тип машины: ", desc.get_sedan())
print("Год машины: ", desc.get_enter())
print()