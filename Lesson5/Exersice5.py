'''numbers = [1, 1, 5, 33, 99, 156, 1, 78]
numbers2 = []

for numbers in numbers:
    if numbers not in numbers2:
        numbers2.append(numbers)
print(numbers2)
print("Kоличество повторений дублирующихся элементов:")
'''

numbers = [1, 1, 5, 33, 33, 156, 1, 78]
array_dublicate_values = []
array_dublicate_counts = []
for i in range(0,len(numbers)):
    if numbers.count(numbers[i]) > 1:




'''
print(numbers)
print("Kоличество повторений дублирующихся элементов:", numbers.count(1))
numbers.remove(1)
print(numbers)
'''

