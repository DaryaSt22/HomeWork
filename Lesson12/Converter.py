# 10. Создайте класс Converter с методами kg_to_pounds и miles_to_km.

class Converter:

    def  kg_to_pounds(self, mass):
        return mass * 2,2

    def miles_to_km(self, length):
        return length * 1,609

obj = Converter()
print(obj.kg_to_pounds(10))
print(obj.miles_to_km(10))

