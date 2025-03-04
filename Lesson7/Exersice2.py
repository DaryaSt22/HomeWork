# Дан список чисел. С помощью filter() получить список
# тех элементов из исходного списка, значение которых больше 0.

sequence_list = [1, 5, -9, 11, 0, 56, 9]

def filter_num(i):
    if(i > 0):
        return True
    return False
print(list(filter(filter_num, sequence_list)))
