# Задание 4

numbers = [12, 14, 99, 65, 20, 64]
for i in range(0, 5):
    result = sum(numbers)
print(result)
print(max(numbers))
print(min(numbers))


# Задание №3. Числа Фибоначчи
print("Введите длину ряда")
n = int(input())
f1 = f2 = 1
print(f1, f2, end= '')

for i in range(1, n):
    f1, f2 = f2, f1 + f2
    print(f2, end= ' ')
'''
from itertools import count

# Задание №5
'''
numbers = [1, 1, 5, 33, 99, 156, 1, 78]
numbers2 = []

for numbers in numbers:
    if numbers not in numbers2:
        numbers2.append(numbers)
print(numbers2)
print("Kоличество повторений дублирующихся элементов:", )

