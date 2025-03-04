# Задание №1

import math
print("Введите значение а")
a = int(input())
print("Введите значение b")
b = int(input())
print("Введите значение x")
x = int(input())

# a)
print("Результат вычисления выражения а равен:")
result_a = (((math.pow(a, 2) / 3) + (math.pow(a, 2) + 4) / b) + math.sqrt(math.pow(a, 2) + 4) / 4
+ math.sqrt(math.pow((math.pow(a,2) + 4),3)) / 4)
print(result_a)

# b)
result_b = math.cos(x) + math.sin(x)
print("Результат вычисления выражения b равен:")
print(result_b)

# c)
print("Результат вычисления выражения c равен:")
print(math.cbrt((math.pow(math.cos(math.pow(x,2)),2)) + math.pow(math.sin((2 * x) - 1),2)))

# d)
print("Результат вычисления выражения d равен:")
print(((5 * x) + (3 * math.pow(x,2) * math.sqrt(1 + math.pow(math.sin(x),2)))))

# Задание № 2

import math

''' "Играл с кредитами - проиграл"
m - ежемесячная выплата
i - годовая процентная ставка
p - месячная процентная ставка (11,5)
s - cумма займа
n - количество месяцев, на которые взят кредит '''

print("Введите годовую процентную ставку:")
i = float(input())
print("Введите cумма займа:")
s = int(input())
print("Введите количество месяцев, на которые взят кредит:")
n = int(input())
p = float(11.5)
print("Ежемесячная выплата составляет:")
m = (s * p * math.pow((1 + p), n)) / (math.pow((1 + p), n) - 1)
print(m)
print("Итоговые выплаты банку:")
sum_of_payments = m * n
print(sum_of_payments)
print("Переплата составляет:")
print(sum_of_payments - s)

# "Интерстерллар"
''' L - длина года на планете
R - радиус орбиты планеты
v - орбитальная сkорость '''

import math

print("Введите радиус первой планеты:")
r = float(input())
print("Введите орбитальную сkорость первой планеты:")
v = float(input())
first_planet_year_lenth = (2 * r * math.pi) / v
print("Длина года на первой планете:")
print(first_planet_year_lenth)
print("Введите радиус второй планеты:")
r = float(input())
print("Введите орбитальную сkорость второй планеты:")
v = float(input())
second_planet_year_lenth = (2 * r * math.pi) / v
print("Длина года на второй планете:")
print(second_planet_year_lenth)
print("Правда, что на первой планете год больше, чем на второй?")
if first_planet_year_lenth > second_planet_year_lenth:
    print(True)
else: print(False)




