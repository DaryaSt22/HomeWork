# Преобразование строки в число:** Запросить у пользователя строку и
# # попытаться преобразовать её в float, обработав ValueError.
#
# try:
#     str1 = input()
#     num1 = float(str1)
#     print(num1)
# except ValueError:
#     print("Неверный тип")
#
#
# import base64
#
# # Исходный текст
# original_data = "Привет, мир!"
#
# # Кодирование данных в base64
# encoded_data = base64.b64encode(original_data.encode('utf-8'))
# print(f"Закодированные данные: {encoded_data}")
#
# # Декодирование данных обратно в исходный текст
# decoded_data = base64.b64decode(encoded_data).decode('utf-8')
# print(f"Декодированные данные: {decoded_data}")

# Лекция урока №9
# Директория — это просто папка на компьютере.
# В Python директория — это место, где хранятся файлы и другие папки.

import os

print("Current directory:", os.getcwd())
# Это команда, которая показывает, в какой папке (директории) сейчас работает программа

print(os.path.exists("Homework.py"))
# Эта команда отвечает на вопрос: "Есть ли такой файл или папка?"

path = os.path.join("data", "Readme.md")
print(os.path.exists(path))
# Эта команда помогает правильно создать путь к файлу или папке,
# чтобы он работал и на Windows (\), и на Linux/Mac (/).

print(os.listdir())
# Покажет файлы и папки в текущей директории

#print(os.mkdir("Новая_папка"))
# Создаст папку "Новая_папка" в текущем месте

# print(os.rmdir("Новая_папка"))

# Чтобы удалить папку, созданную с помощью os.mkdir("Новая_папка"),
# в Python можно использовать os.rmdir(). os.rmdir() работает только если папка пустая.
# Если в ней есть файлы — выдаст ошибку. Если папка не пустая, используй shutil.rmtree()
# shutil.rmtree() удаляет файлы без возможности восстановления, поэтому используй его аккуратно.

files = os.listdir()  # Показывает файлы и папки в текущей директории
print(files)

open("Exersice1", "w").write("Lesson8")
print(os.stat("Exersice1").st_ctime)

data_for_write = ["записать какие-либо данные в файл", "baby", "see", "missing"]
with open("some_file_to_write.txt", "a") as text_file:
    text_file.writelines(line + "\n" for line in data_for_write) # cпросить

print(data_for_write)