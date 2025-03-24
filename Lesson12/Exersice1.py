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

    def __add__(self, other):
        if isinstance(other, Item):
            return self.get_private_cost + other.get_private_cost
        elif isinstance(other, (int, float)):
            return self.get_private_cost + other
        raise TypeError("Можно складывать только объекты Item")

    # Позволяет использовать item в sum() с начальным значением 0
    def __radd__(self, other):
        if other == 0:
            return self.get_private_cost
        return self.__add__(other)


# Класс «Склад» содержит закрытый массив товаров.
# Обеспечить следующие возможности:

# 4. перегруженная операция сложения товаров по цене

class Storage:

    def __init__(self, items: list[Item]):
        self.items_list = items

        # for i in args:
        #     self.items_list.append(Good(i))

    def print_items(self):
        for item in self.items_list:
            print(item.info())

# 1. вывод информации о товаре со склада по индексу
    def __getitem__(self, i):
        return self.items_list[i].info()

# 2. вывод информации о товаре со склада по имени товара
    def good_info(self, goods_name):
        try:
            for item in self.items_list:
                if item.get_private_name == goods_name:
                    print(item.info())
        except:
            print("Item not found")

# 3. сортировка товаров по названию, по магазину и по цене
    def items_sort_by_name(self):
        self.items_list.sort(key=lambda item: item.get_private_name)

    def items_sort_by_shops(self):
        self.items_list.sort(key=lambda item: item.get_private_shop)

    def items_sort_by_cost(self):
        self.items_list.sort(key=lambda item: item.get_private_cost)

# 4. перегруженная операция сложения товаров по цене
    def calculate_sum_cost_of_items(self):
        return sum(self.items_list, 0)

item1 = Item ("Trousers", "Jeans", 5556)
item2 = Item ("B-shirt", "Shirts", 457)
item3 = Item ("A-shirt", "A-Shirts", 57)
storage1 = Storage([item1, item2, item3])
# print(storage1.__getitem__(0))
# storage1.good_info("Trousers")
storage1.print_items()
print("___________________________________")
storage1.items_sort_by_name()
storage1.print_items()
print("___________________________________")
storage1.items_sort_by_shops()
storage1.print_items()
print("___________________________________")
storage1.items_sort_by_cost()
storage1.print_items()
print("___________________________________")
print(storage1.calculate_sum_cost_of_items())

