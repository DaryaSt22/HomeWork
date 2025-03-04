# Реализовать программу для подсчёта индекса массы тела человека
# Индекс массы тела измеряется в кг/м² и рассчитывается по формуле: ИМТ = m/h2, где:
# m — масса тела в килограммах,
# h — рост в метрах.

def enter_mass ():
    try:
        m = float(input("Введите массу тела человека: "))
        if m < 1:
            print("Введенное значение меньше или равно 0")
            enter_mass()
    except:
        print("Введенная строка не число. Введите число.")
        enter_mass()
    return m

def enter_height ():
    try:
        h = float(input("Введите рост человека в метрах: "))
        if h < 1:
            print("Введенное значение меньше или равно 0")
            enter_mass()
    except:
        print("Введенная строка не число. Введите число.")
        enter_height()
    return h

def calculate_index_mass ():
    mass = enter_mass()
    height = enter_height()
    print("Индекс массы тела равен: ", mass / (height ** 2))

calculate_index_mass()
