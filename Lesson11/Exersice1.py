# class Soda:
#     def __init__(self, flavor, regular):
#         self.flavor = flavor
#         self.regular = regular
#
#
# #  Реализовать метод строковой репрезентации,
# #  который возвращает строку вроде «У вас газировка с <клубничным> вкусом»
#
#     def __repr__(self):
#         return f"Soda(flavor='{self.flavor}')"
#
# # Если вкус не задан,
# # метод должен возвращать строку «У вас обычная газировка»
#
#     def __str__(self):
#         return f"{self.regular}"
#
# p = Soda("У вас газировка с клубничным вкусом", "У вас обычная газировка")
#
# print(repr(p))
# print(str(p))

class Soda:
    def __init__(self, flavor):
        self.flavor = flavor

    # def __new__(cls):
    #     return super(Soda, cls).__new__()


#  Реализовать метод строковой репрезентации,
#  который возвращает строку вроде «У вас газировка с <клубничным> вкусом»


# Если вкус не задан,
# метод должен возвращать строку «У вас обычная газировка»

    def __str__(self):
        if self.flavor != None:
            return f"У вас газировка с <'{self.flavor}'> вкусом"
        else:
            return "У вас обычная газировка"

p = Soda("клубничный")
d = Soda("малиновый")
p.flavor = None

print(str(p))
print(str(d))