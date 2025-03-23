# 5. Создайте класс BankAccount с атрибутами owner и balance, добавьте метод
# deposit(amount), который увеличивает баланс, и withdraw(amount), который уменьшает баланс

class BankAccount:

    def __init__(self, owner, balance, amount):
        self.owner = owner
        self.balance = balance
        self.amount = amount

    def deposit(self, amount):
        self.amount = amount
        return self.balance + amount

    def withdraw(self, amount):
        self.amount = amount
        return  self.balance - amount

a = BankAccount("Bob", 52000, 1523)
print(a.deposit(152000))
print(a.withdraw(1456))