#4. Создайте класс Laptop с атрибутами brand и price.
# Добавьте метод discount, который уменьшает цену на заданный процент.

class Laptop:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def discount(self, percent):
        return self.price - self.price * (percent/100)

product = Laptop("Lee", 100)
print(product.discount(10))