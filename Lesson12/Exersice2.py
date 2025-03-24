# Экземпляр класса инициализируется двумя целыми числами,
# первое относится к пчеле, второе – к слону.


class Animals:
    def __init__(self, bee, elef):
        self.bee = bee # Первое целое число (пчела)
        self.elef = elef # Второе целое число (слон)

    def bee_change(self, value):
        if self.bee + value > 100:
            self.bee = 100
        elif self.bee + value < 1:
            self.bee = 0
        else:
            self.bee += value

    def elef_change(self, value):
        if self.elef + value > 100:
            self.elef = 100
        elif self.elef + value < 1:
            self.elef = 0
        else:
            self.elef += value

    # fly() – возвращает True, если часть пчелы не меньше части слона, иначе – False
    def fly(self):
        if self.bee >= self.elef:
            return True
        else:
            return False

    # trumpet() – если часть слона не меньше части пчелы,
    # возвращает строку “tu-tu-doo-doo”, иначе – “wzzzz”
    def trumpet(self):
        if self.elef >= self.bee:
            return  "tu-tu-doo-doo"
        else:
            return "wzzzz"

    # eat(meal, value) – может принимать в meal только ”nectar”
    # или “grass”. Если съедает нектар, то value вычитается из
    # части слона, пчеле добавляется. Иначе – наоборот. Не
    # может увеличиваться больше 100 и уменьшаться меньше 0.

    def eat(self, meal, value):
        if meal == "nectar":
            self.bee_change(value)
            self.elef_change(-value)
        elif meal == "grass":
            self.bee_change(-value)
            self.elef_change(value)

bee_elef = Animals (51, 50)
print(f"bee part = {bee_elef.bee}, elef part = {bee_elef.elef}")
print(bee_elef.fly())
print(bee_elef.trumpet())
print("feed elef")
bee_elef.eat("grass", 100)
print(f"bee part = {bee_elef.bee}, elef part = {bee_elef.elef}")
print(bee_elef.trumpet())
print("feed bee")
bee_elef.eat("nectar", 100)
print(f"bee part = {bee_elef.bee}, elef part = {bee_elef.elef}")
print(bee_elef.trumpet())