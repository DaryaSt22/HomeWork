# В отделе работают 3 сотрудника, которые получают заработную плату в рублях.
# Требуется определить: на сколько зарплата самого высокооплачиваемого из них
# отличается от самого низкооплачиваемого.
# В единственной строке входного файла INPUT.TXT записаны размеры зарплат
# всех сотрудников через пробел.
# Каждая заработная плата – это натуральное число, не превышающее 105.
# В выходной файл OUTPUT.TXT необходимо вывести одно целое число
# — разницу между максимальной и минимальной зарплатой.

m1, m2, m3 = map(int, input().split())
a = max(m1, m2, m3)
b = min(m1, m2, m3)
print(a - b)