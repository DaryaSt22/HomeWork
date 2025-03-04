# Напишите программу, которая считывает текст из
# файла (в файле может быть больше одной строки) и выводит
# в новый файл самое часто встречаемое слово в каждой
# строке и число – счётчик количества повторений этого слова в строке.

import re
from collections import Counter

def add_text_of_file(file_name, string):
    with open(file_name, "r", encoding="utf-8") as file:
        content = file.read()
    new_content = content + "\n" + str(string.most_common(1))
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(new_content)

with open("old_text.txt", "r", encoding="utf-8") as file:
    content = file.read()
lines = content.splitlines()
for line in lines:
    words = re.findall(r"\w+", line.lower())
    word_count = Counter(words)
    add_text_of_file("new_file.txt", word_count)