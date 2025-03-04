import re

# Запрещённые слова, разделённые символом
# пробела, должны храниться в файле stop_words.txt

# Напишите программу, которая получает на вход строку
# с названием текстового файла и выводит на экран
# содержимое этого файла

# заменяя все запрещённые слова
# звездочками.
# Программа должна находить
# запрещённые слова в любом месте файла, даже в середине
# другого слова. Замена независима от регистра: если в списке
# запрещённых есть слово exam, то замениться должны exam,
# eXam, EXAm и другие вариации.


# Считать строку из консоли
# Проверить существует ли такой файл с таким названием
# Открыть файл (stop words, достать из него все стоп-слова. splitlines)
# Открыть "файл с названием из консоли" и извелечь его содержимое

# Пройтись по содержимому, каждым стоп-словом по отдельности. Находись совпадения независимо от регистра текста. Все
# найденные вхождения заменить на звездочки

file_name = input("Введите название файла: ")
file_name = "text_file.txt"
try:
    with open(file_name, "r", encoding= "utf-8") as file:
        content = file.read()
except:
    print("Такого файла не существует")

try:
    with open("stop_words.txt", "r") as file:
        stop_words = file.read().splitlines()
except:
    print("Такого файла не существует")

# for word in stop_words:
#     edited_content = content.replace(word, "*")
#     with open(file_name, "w", encoding="utf-8") as file:
#         file.write(edited_content)
list_from_content = content.split(" ")
print(list_from_content)
for word in stop_words:
    for list_word in list_from_content:
        if (
                (list_word.lower() == word) or
                (list_word.lower() == word + ".") or
                (list_word.lower() == word + ",") or
                (list_word.lower() == word + "?") or
                (list_word.lower() == word + "!") or
                (list_word.lower() == word + ":") or
                (list_word.lower() == word + ";") or
                (list_word.lower() == word + "...")):
            # найти индекс элемента, по которому находится list_word

            list_from_content = list_from_content[].replace(list_word, "*")
print(list_word)
edited_content = content.replace(word, "*")
with open(file_name, "w", encoding="utf-8") as file:
    file.write(" ".join(edited_content))

with open(file_name, "r", encoding= "utf-8") as file:
    print(file.read())


