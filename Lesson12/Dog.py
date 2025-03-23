# 2. Создайте класс Dog с атрибутом name.
# Создайте объект класса и измените его атрибут name

class Dog:
    def __init__(self, name = "Dolly"):
        self.name = name

obj = Dog ()
print(obj.name)
obj.name = "Masha"
print(obj.name)