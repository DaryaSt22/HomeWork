# 1. Создайте класс Book с атрибутами title и author.
# Затем создайте объект этого класса и выведите его атрибуты.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def info(self):
        return f"Book: {self.title} {self.author}"

obj = Book("Holms", "Sir Arthur Conan Doyle")
print(obj.info())