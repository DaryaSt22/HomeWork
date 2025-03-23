# 8. Создайте класс Lamp, который хранит состояние (включена или выключена) и метод
# switch(), меняющий состояние

class Lamp:

    def __init__(self):
        self.is_on = False

    def state(self):
        if self.is_on == False:
            print("Лампочка выключена")
        else:
            print("Лампочка включена")

    def switch(self):
        self.is_on = not self.is_on

a = Lamp()
a.state()
a.switch()
a.state()
a.switch()
