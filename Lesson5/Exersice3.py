print("Введите длину ряда:")
n = int(input())
print("Последовательность чисел:")
f1 = 1
f2 = 1
print(f1, f2, end= ' ')

buffer_element = 0
for i in range(1, n):
    buffer_element = f1
    f1 = f2
    f2 = buffer_element + f2
    print(f2, end= ' ')


# Числа Фибоначчи реkурсивным способом
# def F(n):
#     if n in(1, 2):
#         return 1
#     else:
#         return F(n-1) + F(n-2)
# print(F(7))