# 4. Создайте класс Dog с атрибутами name и breed, добавьте метод bark(), который
# печатает "Гав-гав!"

class Dog:

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return f"Собаку зовут: {self.name}, порода собаки: {self.breed}, и она лает: ""Гав-гав!"

doggy = Dog("Bob", "pug")
print(doggy.bark())