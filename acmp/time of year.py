# В выходной файл OUTPUT.TXT выведите для летних месяцев значение «Summer»,
# для зимних – «Winter», для весенних – «Spring», для осенних – «Autumn».
# Если число не соответствует возможному значению месяца,
# то в этом случае следует вывести «Error».
#
number = int(input())
if number in (12, 1, 2):
    print("Winter")
elif number in (3, 4, 5):
    print("Spring")
elif number in (6, 7, 8):
    print("Summer")
elif number in (9, 10, 11):
    print("Autumn")
else:
    print("Error")


