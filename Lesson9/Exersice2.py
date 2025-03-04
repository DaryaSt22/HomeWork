# Замена имён в судебном решении
old = "Эверт-Колокольцева Елизавета Александровна"
with open("Name.txt", "r", encoding="utf-8") as file:
    content = file.read()
content = content.replace(old, "N")
with open("Name.txt", "w", encoding="utf-8") as file:
    file.write(content)
print(content)


