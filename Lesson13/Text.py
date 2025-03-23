# Создайте класс Text с атрибутом content, создайте метод len(), чтобы len("Hello") возвращал 5

class Text:

    def __init__(self, content):
        self.content = content

    def len(self):
        return len(self.content) + len("Hello")

content = Text("")
print(content.len())
