# 12. Создайте класс Employee, который принимает name и salary.
# Добавьте метод info, который выводит данные сотрудника.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def info(self):
        print(self.name, self.salary)

a = Employee("Masha", 5000)
a.info()