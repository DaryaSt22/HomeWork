# Класс «Товар» содержит следующие закрытые поля:
# название товара
# название магазина, в котором подаётся товар
# стоимость товара в рублях

class Item:

    def __init__(self, name, shop, cost):
        # закрытые поля
        self.__name = name
        self.__shop = shop
        self.__cost = cost

    @property
    def get_private_name(self):
       return self.__name

    @property
    def get_private_shop(self):
        return self.__shop

    @property
    def get_private_cost(self):
        return self.__cost

    def info(self):
        return f"Item name = {self.get_private_name}, Item shop = {self.get_private_shop}, Item cost = {self.get_private_cost}"

# Класс «Склад» содержит закрытый массив товаров.
# Обеспечить следующие возможности:
# 3. сортировка товаров по названию, по магазину и по цене
# 4. перегруженная операция сложения товаров по цене

class Storage:

    def __init__(self, items):
        self.items_list = list[Item](items)

        # for i in args:
        #     self.items_list.append(Good(i))

# 1. вывод информации о товаре со склада по индексу
    def __getitem__(self, i):
        return self.items_list[i]

# 2. вывод информации о товаре со склада по имени товара
    def good_info(self, goods_name):
        try:
            index = self.items_list.index(goods_name)
            print(self.items_list[index].info())
        except:
            print("Item not found")

# obj = Good("Trousers", "Wooll", 50000)
# print("Вывод информации о товаре со склада по имени товара: ", obj.get_private_var)

    #
    # def __add__(self, other):
    #         if isinstance(other, Good):
    #             return self.__cost + other.cost
    #         raise TypeError("Сложение возможно только между объектами Good")
    #
    # def __repr__(self):
    #         return f"Good({self.name, self.cost})"


item1 = Item ("Trousers", "Jeans", 5556)
item2 = Item ("T-shirt", "Shirts", 457)
storage1 = Storage([item1, item2])
storage1.good_info("Trousers")
print(storage1.items_list[1])



