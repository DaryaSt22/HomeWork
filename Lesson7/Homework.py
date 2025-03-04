# Сложение всех чисел от 1 до N**
# Напишите функцию sum_up_to(n: int) -> int, которая возвращает сумму всех чисел от 1 до n.


def sum_up_to(n: int) -> int:
    summ = 0
    for i in range(1, n + 1):
        summ = summ + i
    return summ
print(sum_up_to(10))
