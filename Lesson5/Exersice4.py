numbers = [12, 14, 99, 65, 20, 64, 200]
for i in range(1, len(numbers)):
    result = sum(numbers)
print("Сумма всех элементов массива:")
print(result)
print("Максимальный элемент массива (функция):")
print(max(numbers))
print("Минимальный элемент массива (функция):")
print(min(numbers))

# Max array element search realisation
buffer_element = 0
for i in range(1, len(numbers)):
    if buffer_element < numbers[i]:
        buffer_element = numbers[i]
print("Максимальный элемент массива(цикла):")
print(buffer_element)

# Min array element search realisation
buffer_element = numbers[0]
for i in range(1, len(numbers)):
    if buffer_element > numbers[i]:
        buffer_element = numbers[i]
print("Минимальный элемент массива(цикла):")
print(buffer_element)


