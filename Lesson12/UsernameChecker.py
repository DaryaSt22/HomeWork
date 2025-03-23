# 17. Создайте класс UsernameChecker с методом is_valid(username), который
# проверяет, состоит ли имя пользователя только из букв и цифр

class UsernameChecker:

    def __init__(self, name):
        self.name = name

    def is_valid(self, username):
        self.username = username
        if username == isdigit(username):
            print("True")
        elif