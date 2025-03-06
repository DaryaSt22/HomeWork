
class Math:
    def __init__(self):
        pass

    def addition(self, a, b):
        return a + b

    def subtraction(self, a, b):
        return a - b

    def multiplication(self, a, b):
        return a * b

    def division(self, a, b):
        return a / b

call = Math()

print("Сложение: ", call.addition(20,5))
print("Вычитание: ", call.subtraction(20,5))
print("Умножение: ", call.multiplication(20,5))
print("Деление: ", call.division(20,5))