# 7. Создайте класс BankAccount с атрибутами balance и методом deposit, который увеличивает баланс

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, deposit):
        self.balance = self.balance + deposit

    def get_balance(self):
        return self.balance

bank = BankAccount(123000)
print(bank.get_balance())
bank.deposit(1)
print(bank.get_balance())
