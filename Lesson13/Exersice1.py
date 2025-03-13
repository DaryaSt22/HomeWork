# Реализовать программу для вывода
# последовательности чисел Фибоначчи до определённого
# числа в последовательности. Номер числа, до которого нужно
# выводить, задаётся пользователем с клавиатуры. Для
# реализации последовательности использовать генераторную функцию

def my_generator(limit):
    current_elemnt = 1
    f1 = 1
    f2 = 1
    while current_elemnt <= limit:
        if current_elemnt <= 2:
            yield f1
            current_elemnt += 1
        else:
            yield f1 + f2
            buffer_element = f1
            f1 = f2
            f2 = buffer_element + f2
            current_elemnt +=1

generator = my_generator(int(input("Введите номер элемента последовательлности чселл Фибоначчи, до которрого "
                                   "необходимо вывести последовательность: ")))
# print(generator)
for i in generator:
    print(i, end=" ")