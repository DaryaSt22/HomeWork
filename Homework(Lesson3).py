# Задание №1. Целочисленные переменные

one = int(165)
two = int(35)
three = int(50)
summa = one + two + three
print(summa)
different = one - two - three
print(different)
multiplication = one * two * three
print(multiplication)
result1 = (one - two) + three
print(result1)
result2 = (one * two) / three
print(result2)
result3 = (one + two) % three
print(result3)

#Задание №2. Прямоугольный треугольник
import math
cat_a = int(3)
cat_b = int(4)
square = (cat_a * cat_b) // 2
print(square)
hypotenuse = math.sqrt((cat_a * cat_a) + (cat_b * cat_b)) ** 0.5
print(hypotenuse)

#Задание №3. Определить сколько слов в строке
print("Введите, пожалуйста, текст")
text = input()
words = text.split()
print(len(words))


#Задание №4.Дана строка, заменить в этой строке все появления буквы h на букву H,
# кроме первого и последнего вхождения.
text_one = "hhhabchghhh"
text_one = text_one.replace("hhhabchghhh","hHHabcHgHHh")
print(text_one)

#Задание №5. Действия со строкой
txt = "Hello"
print(txt[2])
print(txt[3]) # -2
print(txt[:5])
print(txt[:3]) # -2
print(txt[::2])
print(txt[1:3]) #1::2
print(txt[::-1])
print(txt[::-2])
print(len(txt))

#Задание №6.Последняя цифра целого числа
print(input()[-1])

#Задание №7. Найти количество десятков трехзначного числа
n = int(input())
print(n // 10 % 10)

#Задание №8. Сумма цифр трехзначного числа
number = input()
a = int(number[0])
b = int(number[1])
c = int(number[2])
print(a + b + c)

