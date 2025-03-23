# 9. Создайте класс Book, который принимает title, author и year, и метод get_info(),
# возвращающий информацию о книге.


class Book:

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        return f"Book: {self.title} {self.author} {self.year}"

obj = Book("Holms", "Sir Arthur Conan Doyle", 1887)
print(obj.get_info())
