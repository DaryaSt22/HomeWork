# *Преобразование кортежа в список**
# Дана структура данных в виде кортежа. Преобразуйте его в список, измените
# один из элементов и снова преобразуйте в кортеж.

nums_tuple = (1, 2, 3, 4, 5)
nums_list = list(nums_tuple)
nums_list[-1] = 6
nums_tuple = tuple(nums_list)
print(nums_tuple)