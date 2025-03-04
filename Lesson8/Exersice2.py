# Реализовать программу с функционалом калькулятора для операций над двумя числами

# Функция для ввода числа

def int_input ():
    try:
        number = int(input("Введите число: "))
    except:
        print("Введенная строка не число. Введите число.")
        return int_input()
    return number

def addition(operand_one, operand_two):
    return operand_one + operand_two

def substruction(operand_one, operand_two):
    return operand_one - operand_two

def multiplication(operand_one, operand_two):
    return operand_one * operand_two

def devide(operand_one, operand_two):
    try:
        return operand_one / operand_two
    except:
        print("Деление на ноль")

def operation_switcher (operand_one, operand_two):
    operation = input("Введите операцию: ")
    match operation:
        case "+":
            print(addition(operand_one, operand_two))
        case "-":
            print(substruction(operand_one, operand_two))
        case "*":
            print(multiplication(operand_one, operand_two))
        case "/":
            print(devide(operand_one, operand_two))
        case _:
            print("Вы ввели неверную операцию! Введите операцию заново!")
            operation_switcher(operand_one, operand_two)

def exit_calculator ():
    answer = input("Вы хотите завершить работу калькулятора? (Да/Нет)")
    if (answer == "Да"):
        print("Калькулятор завершает работу")
        return None
    elif answer == "Нет":
        calculator()
    else:
        exit_calculator()

def calculator():
    print("Калькулятор")
    operand_one = int_input()
    operand_two = int_input()
    operation_switcher(operand_one, operand_two)
    exit_calculator()

calculator()
