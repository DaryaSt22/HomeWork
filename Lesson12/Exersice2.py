# Экземпляр класса инициализируется двумя целыми числами,
# первое относится к пчеле, второе – к слону.

class Animals:
    def __init__(self, x, y):
        self.x = x # Первое целое число (пчела)
        self.y = y # Второе целое число (слон)

    # fly() – возвращает True, если часть пчелы не меньше части слона, иначе – False

    def fly(self):
        if self.x >= self.y:
            print(True)
        else:
            print(False)

    # trumpet() – если часть слона не меньше части пчелы,
    # возвращает строку “tu-tu-doo-doo”, иначе – “wzzzz”

    def trumpet(self):
        if self.y >= self.x:
            print("tu-tu-doo-doo")
        else:
            print("wzzzz")

    # eat(meal, value) – может принимать в meal только ”nectar”
    # или “grass”. Если съедает нектар, то value вычитается из
    # части слона, пчеле добавляется. Иначе – наоборот. Не
    # может увеличиваться больше 100 и уменьшаться меньше 0.

    # def eat(self, meal, value):
    #     pass

call = Animals (310, 299)

print(call.__init__(310,299))
print(call.fly())
print(call.trumpet())