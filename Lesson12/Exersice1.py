# Класс «Товар» содержит следующие закрытые поля:
# название товара
# название магазина, в котором подаётся товар
# стоимость товара в рублях

class Good:

    def __init__(self, name = "Trousers", shop = "Wooll", cost = 50000):
        self.items_list = None
        self.__private_var = name # закрытые поля
        self.__shop = shop
        self.__cost = cost

    @property
    def get_private_var(self):
       return self.__private_var

    @property
    def get_private_shop(self):
        return self.__shop

    @property
    def get_private_cost(self):
        return self.__cost


# Класс «Склад» содержит закрытый массив товаров.
# Обеспечить следующие возможности:
# 3. сортировка товаров по названию, по магазину и по цене
# 4. перегруженная операция сложения товаров по цене

class Storage:

    def __init__(self, *args):
        self.items_list = list()

        for i in args:
            self.items_list.append(Good(i))

# 1. вывод информации о товаре со склада по индексу
    def __getitem__(self, i):
        return self.items_list[i]

# 2. вывод информации о товаре со склада по имени товара
obj = Good("Trousers", "Wooll", 50000)
print("Вывод информации о товаре со склада по имени товара: ", obj.get_private_var)

    #
    # def __add__(self, other):
    #         if isinstance(other, Good):
    #             return self.__cost + other.cost
    #         raise TypeError("Сложение возможно только между объектами Good")
    #
    # def __repr__(self):
    #         return f"Good({self.name, self.cost})"






