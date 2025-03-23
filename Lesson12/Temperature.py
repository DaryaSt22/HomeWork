# 9. Создайте класс Temperature с методом to_fahrenheit, который переводит градусы Цельсия в Фаренгейты.

class Temperature:
    def __init__(self, degree_of_centigrade):
        self.degree_of_centigrade = degree_of_centigrade

    def to_fahrenheit(self):
        return (self.degree_of_centigrade * 1.8) + 32

tempe = Temperature(23)
print(tempe.to_fahrenheit())