# Создайте класс Box с weight, создайте метод add(), чтобы добавить вес в коробку

class Box:

    def __init__(self, weight):
        self.weight = weight

    def __add__(self, other):
        self.other = int(input())
        return self.weight + self.other

obj = Box(55)
print(obj.__add__(55))


